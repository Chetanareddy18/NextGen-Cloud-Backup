import os
from dotenv import load_dotenv
from azure.storage.blob import BlobServiceClient

# Load environment variables
load_dotenv()

# Fetch values from .env
connection_string = os.getenv("AZURE_CONNECTION_STRING")
container_name = os.getenv("CONTAINER_NAME")

# Initialize client
blob_service_client = BlobServiceClient.from_connection_string(connection_string)
container_client = blob_service_client.get_container_client(container_name)

# File to upload
file_path = "test_backup.txt"
blob_name = os.path.basename(file_path)

try:
    with open(file_path, "rb") as data:
        container_client.upload_blob(name=blob_name, data=data, overwrite=True)
    print(f" File '{blob_name}' uploaded successfully to Azure Blob Storage container '{container_name}'.")
except Exception as e:
    print(f" Upload failed: {e}")
