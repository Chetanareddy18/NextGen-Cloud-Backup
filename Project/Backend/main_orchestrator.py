# 9_main_orchestrator.py
import os
from ransomware_layer import is_probably_encrypted
from upload_to_azure import upload_to_azure
from upload_to_aws import upload_to_aws
from verify_integrity import verify_integrity
from corrupt_simulate import corrupt_file
from failover_restore import failover_restore
from download_local import download_from_aws

# === Step 0: Get file from user ===
file_path = input("\nEnter the path of the file to back up (e.g., demo_backup.txt): ").strip()

if not os.path.exists(file_path):
    print(f"File not found: {file_path}")
    exit(1)

print("\n Starting Backup Workflow...")

# === Step 1: Ransomware Entropy Check ===
try:
    if is_probably_encrypted(file_path):
        print(f"File '{file_path}' looks encrypted! Aborting backup.")
        exit(1)
    else:
        print(f"{file_path} passed ransomware check.")
except Exception as e:
    print(f"Error scanning {file_path}: {e}")

# === Step 2: Upload to Azure ===
azure_ok = upload_to_azure(file_path)
if not azure_ok:
    print(" Azure upload failed.")
else:
    print("Uploaded to Azure successfully.")

# === Step 3: Upload to AWS ===
aws_ok = upload_to_aws(file_path)
if not aws_ok:
    print(" AWS upload failed.")
else:
    print("Uploaded to AWS successfully.")

# === Step 4: Verify Integrity ===
try:
    verify_integrity(file_path, file_path)
except Exception as e:
    print(f"Integrity check warning: {e}")

# === Step 5: Simulate Corruption in Azure ===
corrupt_file(file_path)

# === Step 6: Failover Restore from AWS ===
restored_file = failover_restore(file_path)

# === Step 7: Local Download ===
download_from_aws(file_path)

# === Step 8: Re-upload restored file to Azure ===
restored_path = f"restored_{file_path}"
if os.path.exists(restored_path):
    print(f" Re-uploading restored file '{restored_path}' back to Azure...")
    reupload_ok = upload_to_azure(restored_path)
    if reupload_ok:
        print(f"Restored file '{restored_path}' successfully re-uploaded to Azure.")
    else:
        print(f" Re-upload to Azure failed.")
else:
    print(" Restored file not found, skipping re-upload step.")

