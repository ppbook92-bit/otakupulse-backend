from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests
import os

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# This hides your secrets from the public GitHub page
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")

@app.head("/")
def ping():
    return {"status": "Alive"}

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


@app.get("/test")
def test_vault():
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHANNEL_ID,
        "text": "Test message! The Render bridge is working perfectly."
    }
    requests.post(url, json=payload)
    return {"status": "Test fired! Check Telegram."}

