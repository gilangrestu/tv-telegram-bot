from flask import Flask, request
import requests

BOT_TOKEN = "TOKEN_BOT_ANDA"
CHAT_ID = "CHAT_ID_ANDA"

app = Flask(__name__)

@app.route("/", methods=["POST"])
def webhook():

    data = request.json

    requests.post(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        json={
            "chat_id": CHAT_ID,
            "text": str(data)
        }
    )

    return "OK"

@app.route("/", methods=["GET"])
def home():
    return "Running"
