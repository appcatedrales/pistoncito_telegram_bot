import os
from flask import Flask
import telegram

app = Flask(__name__)

@app.route("/")
def home():
    return "Pistoncito está online 🚀"

@app.route("/mensaje_prueba")
def enviar_mensaje():
    TOKEN = os.getenv("BOT_TOKEN")
    CHAT_ID = os.getenv("CHAT_ID")
    bot = telegram.Bot(token=TOKEN)
    bot.send_message(chat_id=CHAT_ID, text="✅ Pistoncito dice: estoy funcionando y puedo enviarte mensajes.")
    return "Mensaje enviado ✅"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
