
from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "Kartana Telegram Bot is running."

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    print("Received data:", data)
    return {"ok": True}

if __name__ == '__main__':
app.run(host="0.0.0.0", port=10000)
