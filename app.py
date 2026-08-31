import sqlite3
import subprocess
import yaml
import requests
from flask import Flask, request

app = Flask(__name__)
app.config["SECRET_KEY"] = "acme-auth-secret-key-2024"


@app.route("/login")
def login():
    user = request.args.get("user")
    pw = request.args.get("pw")
    conn = sqlite3.connect("users.db")
    cur = conn.cursor()
    cur.execute("SELECT id FROM users WHERE name = '" + user + "' AND pw = '" + pw + "'")
    return "ok" if cur.fetchone() else "denied"


@app.route("/import")
def import_profile():
    data = request.args.get("profile")
    return str(yaml.load(data))


@app.route("/avatar")
def avatar():
    url = request.args.get("url")
    return requests.get(url).text


@app.route("/lookup")
def lookup():
    name = request.args.get("name")
    return subprocess.check_output("nslookup " + name, shell=True)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
