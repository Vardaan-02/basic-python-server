from flask import request
import datetime

def get_home():
    return "🔥 Hello from Flask!"

def get_health():
    return "✅ Server is up and running!"

def get_about():
    return "This is Vardaan."

def get_time():
    now = datetime.datetime.now()
    return f"🕒 Current server time: {now.strftime('%Y-%m-%d %H:%M:%S')}"

def get_location():
    return "📍 Server location: 🌐 Hosted in the Cloud (or localhost 😅)"

def post_greet():
    data = request.json
    name = data.get("name", "stranger")
    return f"👋 Hello, {name}! Welcome aboard."
