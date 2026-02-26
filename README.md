## 🌩️ NextGen Cloud Backup System
A Cross-Cloud Automatic Backup, Failover & Ransomware-Aware Storage Solution

NextGen Cloud Backup System is a multi-cloud, automated, secure backup framework designed to protect critical files against storage failures, ransomware attacks, and data corruption.
It seamlessly uploads files to both Azure Blob Storage and AWS S3, includes automatic failover, and sends real-time alerts via Email and Microsoft Teams.
The project demonstrates enterprise-grade resilience with a clean UI and intelligent backend.

📑 Table of Contents

Features

- System Architecture

Project Structure

Tech Stack

Installation & Setup

Usage

Configuration

Dashboard

Security Notes

Future Enhancements

Troubleshooting

Author

License

🚀 Features
🔹 Multi-Cloud Backup

Automatically uploads user files to:

Azure Blob Storage

AWS S3

Ensures redundancy and strong disaster recovery.

🔹 Automatic Failover

If Azure upload fails, the system switches to AWS — and vice versa — guaranteeing no data loss.

🔹 Ransomware Detection (Simulated)

Scans uploaded files for suspicious patterns

Can be extended into ML/AI-based anomaly detection

🔹 Real-Time Alerts

Receive immediate notifications for:

Successful uploads

Failover events

Ransomware detection warnings

Backup failures

Delivery channels:

Email (SMTP Gmail)

Microsoft Teams Webhook

🔹 Clean Modern UI

Minimal and responsive interface built with:

HTML5

CSS3

Bootstrap

JavaScript

🔹 Dashboard View

Monitor:

Upload history

Cloud health status

Number of failovers

Alerts triggered

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

Azure Blob Storage

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

Python Dotenv

SMTP (smtplib)

HTTP Requests (requests)

Frontend

HTML5

CSS3

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
Backend:
cd Backend
pip install -r requirements.txt

Frontend:
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


Open your browser:
👉 http://127.0.0.1:5000/

📘 Usage

Open the UI Upload Page

Select a file to back up

System performs:

Ransomware scan

Primary cloud upload

Failover if needed

View results on the Dashboard

Alerts are sent automatically if enabled

⚙️ Configuration
Modify cloud settings

Backend .env controls all credentials for:

Azure Blob

AWS S3

Modify alert settings

You can enable/disable:

Email

Teams Webhooks

Extend ransomware detection

Custom logic lives in:

Backend/cloud_utils.py
Backend/failover_restore.py

📊 Dashboard

Provides insights including:

Upload success/failure summary

Cloud service availability

Failover events

Recent alerts

Easy to extend for:

Graphs

Real-time cloud sync

File version history

⚠️ Security Notes

❌ Never upload .env to GitHub

✔️ Use Azure KeyVault and AWS Secrets Manager for production

✔️ Enforce HTTPS for all data transfer

✔️ Replace simulated ransomware detection with ML/AI models

🌟 Future Enhancements

Planned advanced features:

AI/ML-based ransomware detection

Anomaly detection for abnormal backup behavior

Blockchain-based integrity verification

Quantum-safe encryption

Real-time multi-cloud sync dashboard

User authentication (RBAC)

End-to-end encrypted file backups

🛠️ Troubleshooting
Issue	Possible Cause	Fix
Upload failing	Incorrect cloud credentials	Check .env
No alerts sent	SMTP or Teams URL misconfigured	Confirm credentials
Dashboard not updating	Backend not running	Launch both Flask apps
Failover not triggering	Primary storage still reachable	Simulate cloud outage
👨‍💻 Author

Palla Chetana Reddy
NextGen Cloud Architect & Developer

📝 License

Open-source — free for educational and research use.
