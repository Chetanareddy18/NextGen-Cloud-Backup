# Backend/api_server.py
from fastapi import FastAPI, UploadFile, File
import shutil
from ransomware_layer import ransomware_check
from upload_to_azure import upload_to_azure
from upload_to_aws import upload_to_aws
from verify_integrity import verify_integrity
from corrupt_simulate import corrupt_file
from failover_restore import failover_restore

app = FastAPI()

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    filename = file.filename
    with open(filename, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    logs = []

    if not ransomware_check(filename):
        return {"status": "rejected", "logs": ["Ransomware detected"]}

    upload_to_azure(filename)
    upload_to_aws(filename)
    verify_integrity(filename, filename)
    corrupt_file(filename)
    failover_restore(filename)

    return {"status": "success", "logs": ["Backup complete"]}


