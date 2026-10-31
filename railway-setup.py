import os
import sys

from CTFd import create_app
from CTFd.utils.config import is_setup

name, email, password = (os.environ.get(k, "").strip() for k in ("CTFD_ADMIN_NAME", "CTFD_ADMIN_EMAIL", "CTFD_ADMIN_PASSWORD"))
app = create_app()
with app.app_context():
    if is_setup() or not (name and email and password):
        sys.exit()

client = app.test_client()
client.get("/setup")
with client.session_transaction() as s:
    nonce = s["nonce"]
r = client.post("/setup", data={
    "ctf_name": os.environ.get("CTFD_NAME", "").strip() or "CTF",
    "ctf_description": "",
    "user_mode": "users",
    "name": name,
    "email": email,
    "password": password,
    "ctf_theme": "core",
    "nonce": nonce,
})
with app.app_context():
    print("railway-setup:", f"created admin {name}" if is_setup() else f"setup failed (HTTP {r.status_code})")
