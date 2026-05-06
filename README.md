# NextGen Cloud Backup System
# NextGen Cloud Backup System

## Cross-Cloud Automatic Backup, Failover, and Ransomware-Aware Storage

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Backend-Flask-000000?logo=flask&logoColor=white)
![Azure](https://img.shields.io/badge/Cloud-Azure%20Blob-0078D4?logo=microsoftazure&logoColor=white)
![AWS](https://img.shields.io/badge/Cloud-AWS%20S3-FF9900?logo=amazonaws&logoColor=white)

NextGen Cloud Backup System is a multi-cloud backup framework that protects critical files against storage failures, corruption, and ransomware-like behavior. It supports automated backup to Azure Blob and AWS S3, cloud failover, and real-time alerting via email and Microsoft Teams.

## Features

- Multi-cloud backup to Azure Blob Storage and AWS S3
- Automatic failover between cloud providers
- Simulated ransomware/corruption detection layer
- Real-time alerting for success, failure, failover, and warnings
- Web UI for uploads and dashboard monitoring
- Backend modules for orchestration, integrity checks, and restore

## System Architecture

### Frontend (Flask UI)

- File upload interface
- Dashboard status view
- User-facing result and alert feedback

### Backend (Python Services)

- Upload and failover orchestration
- Ransomware simulation/detection layer
- File integrity verification
- Restore/download operations
- Alert integration

### Cloud and Alerting

- Azure Blob Storage
- AWS S3
- SMTP Email alerts
- Microsoft Teams webhook alerts

## Project Structure

```text
NextGen-Cloud-Backup/
|-- Project/
|   |-- Backend/
|   |   |-- api_server.py
|   |   |-- failover_restore.py
|   |   |-- main_orchestrator.py
|   |   |-- ransomware_layer.py
|   |   |-- upload_to_aws.py
|   |   |-- upload_to_azure.py
|   |   |-- verify_integrity.py
|   |   `-- download_local.py
|   |-- Frontend/
|   |   |-- app.py
|   |   |-- alert_services.py
|   |   |-- dashboard_data.json
|   |   |-- templates/
|   |   `-- static/
|   `-- .env
|-- requirements.txt
`-- README.md
```

## Tech Stack

### Backend

- Python
- Flask
- boto3 (AWS S3)
- azure-storage-blob (Azure Blob)
- python-dotenv
- requests
- smtplib

### Frontend

- Flask templates
- HTML5
- CSS3
- Bootstrap
- JavaScript

## Setup and Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Chetanareddy18/NextGen-Cloud-Backup.git
cd NextGen-Cloud-Backup
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Environment Variables

Create `Project/.env` with your credentials:

```env
AZURE_CONN_STRING=your_azure_storage_connection_string
AZURE_CONTAINER=your_container

AWS_ACCESS_KEY=your_access_key
AWS_SECRET_KEY=your_secret_key
AWS_BUCKET=your_bucket_name

ALERT_EMAIL=youremail@gmail.com
ALERT_EMAIL_PASSWORD=your_generated_app_password
ALERT_RECEIVER=receiver@gmail.com

TEAMS_WEBHOOK_URL=your_teams_webhook_url
FLASK_SECRET=your_secret
```

## Run the Project

### Start Backend Services

```bash
python Project/Backend/main_orchestrator.py
```

### Start Frontend App

```bash
python Project/Frontend/app.py
```

Open in browser:

`http://127.0.0.1:5000/`

## Usage Workflow

1. Upload a file using the UI.
2. System checks for suspicious/corrupted patterns.
3. File uploads to the primary cloud target.
4. If primary fails, automatic failover sends to secondary cloud.
5. Alerts and dashboard records are updated.
6. Restore/verification flow can be executed from backend modules.

## Configuration Notes

- Cloud and alert keys are managed through `Project/.env`.
- Alert logic is implemented in `Project/Frontend/alert_services.py`.
- Backup/failover logic lives in `Project/Backend/failover_restore.py` and `Project/Backend/main_orchestrator.py`.
- Integrity and ransomware simulation are in `Project/Backend/verify_integrity.py` and `Project/Backend/ransomware_layer.py`.

## Security Notes

- Never commit `.env` secrets.
- Use secret managers (Azure Key Vault, AWS Secrets Manager) in production.
- Enforce HTTPS and secure credential rotation.
- Replace simulated detection with production-grade ML anomaly models.

## Future Enhancements

- AI/ML-based ransomware detection
- Real-time multi-cloud sync dashboard
- Role-based authentication (RBAC)
- End-to-end encrypted backups
- Blockchain-backed integrity audit trails

## Troubleshooting

| Issue | Possible Cause | Fix |
| --- | --- | --- |
| Upload fails | Invalid cloud credentials | Verify `Project/.env` keys |
| Alerts not sent | SMTP/Teams config issue | Recheck alert credentials and webhook URL |
| Dashboard stale | Frontend or backend not running | Start both services |
| Failover not triggered | Primary provider still reachable | Simulate provider outage for test |

## Author

Palla Chetana Reddy  
NextGen Cloud Architect and Developer

## License

Open-source for educational and research use.
