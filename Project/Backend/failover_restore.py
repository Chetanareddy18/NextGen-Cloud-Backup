# Backend/failover_restore.py
import os
import boto3
from azure.storage.blob import BlobServiceClient
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def failover_restore(file_name: str):
    """
    Restore a file from AWS S3 to Azure Blob Storage (failover recovery).
    Called when Azure data is lost or corrupted.
    """
    try:
        print("\nDebug: Checking environment vars...")
        conn_str = os.getenv("AZURE_STORAGE_CONNECTION_STRING") or os.getenv("AZURE_CONNECTION_STRING")
        container = os.getenv("AZURE_CONTAINER_NAME") or os.getenv("CONTAINER_NAME")

        aws_access_key = os.getenv("AWS_ACCESS_KEY_ID")
        aws_secret_key = os.getenv("AWS_SECRET_ACCESS_KEY")
        region = os.getenv("AWS_REGION")
        bucket = os.getenv("BUCKET_NAME") or os.getenv("AWS_BUCKET")

        print(f"AZURE_STORAGE_CONNECTION_STRING = {'SET' if conn_str else 'None'}")
        print(f"AZURE_CONTAINER_NAME = {container}")
        print(f"AWS_BUCKET = {bucket}")

        if not conn_str or not container:
            raise ValueError("Azure connection string or container missing in .env")

        if not bucket:
            raise ValueError("AWS bucket name not set in .env")

        # Step 1: Download from AWS
        s3 = boto3.client(
            "s3",
            aws_access_key_id=aws_access_key,
            aws_secret_access_key=aws_secret_key,
            region_name=region
        )

        restored_path = os.path.join(os.getcwd(), f"restored_{file_name}")
        s3.download_file(bucket, file_name, restored_path)
        print(f"Restored '{file_name}' from AWS S3 → saved as '{restored_path}'.")

        # Step 2: Upload again to Azure
        blob_service = BlobServiceClient.from_connection_string(conn_str)
        blob_client = blob_service.get_blob_client(container=container, blob=file_name)

        with open(restored_path, "rb") as data:
            blob_client.upload_blob(data, overwrite=True)

        print(f"Successfully re-uploaded '{file_name}' to Azure container '{container}'.")

        # Step 3: Verify upload
        container_client = blob_service.get_container_client(container)
        blobs = [b.name for b in container_client.list_blobs()]
        if file_name in blobs:
            print(f"Verification success: '{file_name}' is now visible in Azure.")
        else:
            print(f"Upload done but '{file_name}' not visible yet. Check Azure portal manually.")

        return True

    except Exception as e:
        print(f"Failover restore failed: {e}")
        return False


if __name__ == "__main__":
    print(" Testing standalone failover restore...")
    test_file = input("Enter file name to restore from AWS → Azure (e.g. demo.txt): ").strip()
    if not test_file:
        print(" No file entered — exiting.")
    else:
        result = failover_restore(test_file)
        if result:
            print(" Failover restore completed successfully!")
        else:
            print(" Failover restore failed. Check logs above.")
