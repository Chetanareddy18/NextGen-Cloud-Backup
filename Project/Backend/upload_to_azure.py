import os
from azure.storage.blob import BlobServiceClient
from dotenv import load_dotenv

load_dotenv()

def upload_to_azure(file_path: str):
    """Uploads a local file to Azure Blob Storage."""
    try:
        conn_str = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
        container_name = os.getenv("AZURE_CONTAINER_NAME")

        if not conn_str or not container_name:
            raise ValueError("Azure environment variables missing.")

        blob_service_client = BlobServiceClient.from_connection_string(conn_str)
        blob_client = blob_service_client.get_blob_client(container=container_name, blob=os.path.basename(file_path))

        with open(file_path, "rb") as data:
            blob_client.upload_blob(data, overwrite=True)

        print(f"Uploaded '{file_path}' to Azure container '{container_name}'.")
        return True
    except Exception as e:
        print(f"Azure upload failed: {e}")
        return False
