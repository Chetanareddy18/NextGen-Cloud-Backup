import os
import boto3
from dotenv import load_dotenv

load_dotenv()

def download_from_aws(file_name: str):
    """Download file from AWS locally."""
    try:
        s3 = boto3.client(
            "s3",
            aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
            aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
            region_name=os.getenv("AWS_REGION")
        )
        bucket = os.getenv("BUCKET_NAME")
        local_path = f"downloaded_{file_name}"
        s3.download_file(bucket, file_name, local_path)
        print(f"File '{file_name}' downloaded locally as '{local_path}'.")
    except Exception as e:
        print(f"Local download failed: {e}")
