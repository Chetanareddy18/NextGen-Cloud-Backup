import os
import boto3
from dotenv import load_dotenv

load_dotenv()

def upload_to_aws(file_path: str):
    try:
        s3 = boto3.client(
            "s3",
            aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
            aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
            region_name=os.getenv("AWS_REGION")
        )
        bucket = os.getenv("BUCKET_NAME")
        s3.upload_file(file_path, bucket, os.path.basename(file_path))
        print(f"Uploaded '{file_path}' to AWS S3 bucket '{bucket}'.")
    except Exception as e:
        print(f" AWS upload failed: {e}")
