import os
import boto3
from dotenv import load_dotenv

# Step 1: Load AWS credentials and settings from .env file
load_dotenv()

AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_REGION = os.getenv("AWS_REGION")
BUCKET_NAME = os.getenv("BUCKET_NAME")

# Step 2: Initialize S3 client
s3 = boto3.client(
    "s3",
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=AWS_REGION
)

# Step 3: Test file to upload (like your Azure test)
file_path = "azure_failover_backup.txt"   # The file you already created for Azure testing
file_name = os.path.basename(file_path)

try:
    # Step 4: Upload the file to S3 bucket
    s3.upload_file(file_path, BUCKET_NAME, file_name)
    print(f" File '{file_name}' uploaded successfully to AWS S3 bucket '{BUCKET_NAME}'.")
except Exception as e:
    print(f" Upload failed: {e}")
