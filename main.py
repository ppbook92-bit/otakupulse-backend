from fastapi import FastAPI
import requests
import os

app = FastAPI()

# This hides your secrets from the public GitHub page
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")

@app.get("/")
def home():
    return {"status": "OtakuPulse Vault Bridge is Online"}

@app.post("/update_taste")
def update_taste(data: dict):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHANNEL_ID,
        "text": str(data)
    }
    requests.post(url, json=payload)
    return {"status": "success", "message": "Data secured in Vault"}
