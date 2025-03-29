from flask import Flask, request
import requests
import os

TOKEN = "8107463006:AAHFT8n8hj5x5__95uI3BC2f5Yopqz05MO4"
API_URL = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

app = Flask(__name__)

@app.route('/')
def home():
    return "Kartana Telegram Bot is alive."

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    print("Received:", data)

    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        text = data["message"].get("text", "")
        
        reply = "Привет, я Картана. Пока учусь отвечать, но уже здесь."
        
        requests.post(API_URL, json={
            "chat_id": chat_id,
            "text": reply
        })

    return {"ok": True}

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=10000)
