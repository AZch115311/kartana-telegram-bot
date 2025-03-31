from flask import Flask, request
import requests
import os
import json

TOKEN = "8107463006:AAHFT8n8hj5x5__95uI3BC2f5Yopqz05MO4"
API_URL = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

MEMORY_FILE = "memory.json"

def load_memory():
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r") as f:
            return json.load(f)
    return {
        "messages": [],
        "state": {
            "mode": "normal",
            "last_user_input": ""
        }
    }

def save_memory(data):
    with open(MEMORY_FILE, "w") as f:
        json.dump(data, f, indent=2)

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

        # Сохраняем сообщение
        memory = load_memory()
        memory["messages"].append({
            "from": "user",
            "text": text
        })
        memory["state"]["last_user_input"] = text
        save_memory(memory)

        # Ответ
        reply = "Привет, я Картана. Пока учусь отвечать, но уже здесь."
        requests.post(API_URL, json={
            "chat_id": chat_id,
            "text": reply
        })

    return {"ok": True}

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
