import os
import boto3
from azure.storage.blob import BlobServiceClient
from dotenv import load_dotenv

load_dotenv()

# --- Azure config ---
AZURE_CONN = os.getenv("AZURE_CONNECTION_STRING")
AZURE_CONTAINER = os.getenv("CONTAINER_NAME")

# --- AWS config ---
AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_REGION = os.getenv("AWS_REGION")
BUCKET_NAME = os.getenv("BUCKET_NAME")

# --- Initialize clients ---
azure_client = BlobServiceClient.from_connection_string(AZURE_CONN)
s3 = boto3.client(
    "s3",
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=AWS_REGION
)

file_name = "azure_failover_backup.txt"
restore_path = f"restored_{file_name}"

# --- Step 1: Check Azure ---
try:
    container = azure_client.get_container_client(AZURE_CONTAINER)
    blob_list = list(container.list_blobs(name_starts_with=file_name))
    if blob_list:
        print("Azure is healthy, file present — no failover needed.")
    else:
        raise Exception("File not found in Azure container.")
except Exception as e:
    print(f"Azure check failed ({e}). Initiating AWS failover...")

    # --- Step 2: Pull backup from AWS ---
    try:
        s3.download_file(BUCKET_NAME, file_name, restore_path)
        print(f" Restored '{file_name}' from AWS as '{restore_path}'.")

        # --- Step 3: Re-upload to Azure when back online ---
        try:
            blob_client = container.get_blob_client(file_name)
            with open(restore_path, "rb") as data:
                blob_client.upload_blob(data, overwrite=True)
            print("File re-uploaded to Azure once connection restored.")
        except Exception as reupload_error:
            print(f"Skipped re-upload (Azure still down): {reupload_error}")

    except Exception as aws_error:
        print(f" AWS restore failed: {aws_error}")
