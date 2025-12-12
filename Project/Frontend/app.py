# Frontend/app.py
import os
import sys
import json
from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename
from dotenv import load_dotenv
from alert_services import send_email_alert, send_teams_alert

# Load environment variables (.env)
load_dotenv()

# Add backend path
BACKEND_PATH = os.path.abspath("../Backend")
sys.path.append(BACKEND_PATH)

# Import modules
from ransomware_layer import ransomware_check
from upload_to_azure import upload_to_azure
from upload_to_aws import upload_to_aws
from verify_integrity import verify_integrity
from corrupt_simulate import simulate_corruption
from failover_restore import failover_restore
from alert_services import send_email_alert, send_teams_alert  # ✅ import alerts

app = Flask(__name__)
app.secret_key = "nextgen_secret"
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

DATA_FILE = "dashboard_data.json"

def update_stat(key):
    """Update dashboard metrics."""
    if not os.path.exists(DATA_FILE):
        data = {
            "total_uploads": 0,
            "uploads_azure": 0,
            "uploads_aws": 0,
            "corruptions": 0,
            "restores": 0,
            "ransomware_blocked": 0
        }
    else:
        with open(DATA_FILE, "r") as f:
            data = json.load(f)

    data[key] += 1

    with open(DATA_FILE, "w") as f:
        json.dump(data, f)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload_file():
    if "file" not in request.files:
        flash("No file part!")
        return redirect(url_for("index"))

    file = request.files["file"]
    if file.filename == "":
        flash("No file selected!")
        return redirect(url_for("index"))

    filename = secure_filename(file.filename)
    filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)
    file.save(filepath)

    logs = []
    update_stat("total_uploads")

    # Step 1: Ransomware Check
    if not ransomware_check(filepath):
        logs.append(" Ransomware detected — upload rejected!")
        update_stat("ransomware_blocked")

        # Send alerts
        send_email_alert("🚨 Ransomware Alert", f"Ransomware detected in file: {filename}")
        send_teams_alert(f"🚨 **Ransomware Detected** in `{filename}` — upload blocked!")

        return render_template("index.html", logs=logs)

    logs.append("✅ File passed ransomware check.")

    # Step 2: Upload to Azure + AWS
    try:
        upload_to_azure(filepath)
        logs.append("☁️ Uploaded to Azure (Primary).")
        update_stat("uploads_azure")
    except Exception as e:
        logs.append(f"❌ Azure Upload Failed: {e}")
        send_teams_alert(f"⚠️ Azure Upload Failed for `{filename}`: {e}")
        send_email_alert("⚠️ Azure Upload Failed", str(e))

    try:
        upload_to_aws(filepath)
        logs.append("☁️ Uploaded to AWS (Secondary).")
        update_stat("uploads_aws")
    except Exception as e:
        logs.append(f"❌ AWS Upload Failed: {e}")
        send_teams_alert(f"⚠️ AWS Upload Failed for `{filename}`: {e}")
        send_email_alert("⚠️ AWS Upload Failed", str(e))

    # Step 3: Verify Integrity
    try:
        verify_integrity(filepath, filepath)
        logs.append("✅ Integrity verified — both backups match.")
    except Exception as e:
        logs.append(f"⚠️ Integrity check failed: {e}")
        send_teams_alert(f"⚠️ Integrity Mismatch Detected for `{filename}`")
        send_email_alert("⚠️ Integrity Verification Failed", str(e))

    # Step 4: Simulate corruption + Failover Restore
    try:
        corrupted = simulate_corruption(filepath)
        logs.append(f"💥 Corrupted file simulated: {corrupted}")
        update_stat("corruptions")

        restored = failover_restore(filename)
        if restored:
            logs.append("✅ Restored successfully from AWS → Azure.")
            update_stat("restores")
            send_teams_alert(f"✅ File `{filename}` restored successfully via failover.")
            send_email_alert("✅ Failover Restore Successful", f"File {filename} restored from AWS to Azure.")
        else:
            logs.append("❌ Failover restore failed — check logs.")
            send_teams_alert(f"❌ Failover Restore Failed for `{filename}`")
            send_email_alert("❌ Failover Restore Failed", f"File {filename} could not be restored.")
    except Exception as e:
        logs.append(f"⚠️ Failover restore failed: {e}")
        send_teams_alert(f"⚠️ Failover process error: {e}")
        send_email_alert("⚠️ Failover Error", str(e))

    flash("✅ Backup process complete!")
    return render_template("index.html", logs=logs)

@app.route("/dashboard")
def dashboard():
    with open(DATA_FILE, "r") as f:
        stats = json.load(f)
    return render_template("dashboard.html", stats=stats)

if __name__ == "__main__":
    app.run(debug=True)
