from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "✅ Pistoncito está funcionando sin telegram por ahora"

@app.route("/mensaje_prueba")
def prueba():
    return "✅ Ruta /mensaje_prueba activa (sin telegram todavía)"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
