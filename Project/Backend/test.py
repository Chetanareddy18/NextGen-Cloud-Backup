from azure.storage.blob import BlobServiceClient
from dotenv import load_dotenv
import os

load_dotenv()

conn_str = os.getenv("AZURE_CONNECTION_STRING")
container_name = os.getenv("CONTAINER_NAME")

print("Azure conn str:", conn_str)
print("Container:", container_name)

blob_service = BlobServiceClient.from_connection_string(conn_str)
container_client = blob_service.get_container_client(container_name)

for blob in container_client.list_blobs():
    print(blob.name)
