🌩️ NextGen Cloud Backup System

A Cross-Cloud Automatic Backup, Failover & Ransomware-Aware Storage Solution

NextGen Cloud Backup System is a multi-cloud, automated, secure backup framework designed to protect critical files against storage failures, ransomware attacks, and data corruption.
It uploads files to both Azure Blob Storage & AWS S3, triggers automatic failover, and sends real-time alerts via Email & Microsoft Teams.

This project demonstrates enterprise-grade resilience with a simple UI and intelligent backend.

🚀 Features
🔹 Multi-Cloud Backup

Upload your files and automatically store them in:

Azure Blob Storage

AWS S3

Ensures redundancy and disaster recovery.

🔹 Automatic Failover

If Azure upload fails, the system automatically switches to AWS — and vice-versa — ensuring zero data loss.

🔹 Ransomware Detection (Simulated)

Basic scanning to detect suspicious file patterns.
(You can extend this to ML/AI-based anomaly detection.)

🔹 Real-Time Alerts

Receive notifications for:

Successful backups

Failover events

Backup failures

Ransomware warnings

Alerts delivered through:

Email (SMTP Gmail)

Microsoft Teams Webhook

🔹 Clean Modern UI

A minimal, responsive HTML interface using:

HTML5

CSS3

Bootstrap

JS

🔹 Dashboard View

Monitor:

Upload history

Cloud health status

Number of failovers

Alerts triggered

The dashboard is simple and extendable.

🏛️ System Architecture

Frontend (Flask UI)

Upload page

Dashboard

Alert pop-ups

Backend (Python Flask)

File handling

Cloud upload logic

Failover logic

Ransomware detection

Logging

Alert services

Cloud Providers

Azure Storage

AWS S3

Alert Channels

SMTP Email

Microsoft Teams Webhook

📂 Project Structure
NextGen-Cloud-Backup/
│
├── Backend/
│   ├── failover_restore.py
│   ├── cloud_utils.py
│   ├── alert_services.py
│   ├── requirements.txt
│   └── .env
│
├── Frontend/
│   ├── app.py
│   ├── templates/
│   │     ├── index.html
│   │     ├── dashboard.html
│   │     └── result.html
│   ├── static/
│         ├── css/
│         ├── js/
│         └── images/
│   └── .env
│
└── README.md

🛠️ Tech Stack
Backend

Python 3

Flask

Azure SDK (azure-storage-blob)

AWS Boto3

dotenv

smtplib

requests

Frontend

HTML

CSS

Bootstrap

JavaScript

Cloud

Azure Blob Storage

AWS S3

🔧 Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/yourusername/NextGen-Cloud-Backup.git
cd NextGen-Cloud-Backup

2️⃣ Install Requirements

Go to Backend folder:

cd Backend
pip install -r requirements.txt


Go to Frontend folder:

cd ../Frontend
pip install -r requirements.txt

3️⃣ Create .env Files
Backend .env
AZURE_CONN_STRING=your_azure_storage_connection_string
AZURE_CONTAINER=your_container
AWS_ACCESS_KEY=your_access_key
AWS_SECRET_KEY=your_secret_key
AWS_BUCKET=your_bucket_name

ALERT_EMAIL=youremail@gmail.com
ALERT_EMAIL_PASSWORD=your_generated_app_password
ALERT_RECEIVER=receiver@gmail.com

TEAMS_WEBHOOK_URL=your_teams_webhook_url

Frontend .env
FLASK_SECRET=your_secret

4️⃣ Run the Backend
cd Backend
python failover_restore.py

5️⃣ Run the Frontend
cd Frontend
python app.py


Then open:

http://127.0.0.1:5000/



⚠️ Security Notes

Never upload .env to GitHub.

Use KeyVault (Azure) & Secrets Manager (AWS) for production.

Use HTTPS for data transmission.

Replace simple ransomware detection with ML-based anomaly models.

🌟 Future Enhancements
Planned Advanced Features

AI-based ransomware detection

ML anomaly detection for unusual backups

Blockchain-based integrity verification

Quantum-safe encryption (Post-Quantum Cryptography)

Real-time cloud sync dashboard

User authentication + RBAC

Encrypted file backups

👨‍💻 Author

Palla Chetana Reddy
NextGen Cloud Architect & Developer


📝 License

This project is open-source and free to use for educational and research purposes.