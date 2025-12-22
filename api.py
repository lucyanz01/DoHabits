from dotenv import load_dotenv
load_dotenv()

from flask import Flask
import os
from backend.routes.auth import bp as auth_bp
from backend.routes.dohabits_api import bp_api as api_bp

app = Flask(__name__)

app.register_blueprint(auth_bp, url_prefix="/auth")
app.register_blueprint(api_bp, url_prefix="/api")

@app.route("/")
def home():
    return "API funcionando"

if __name__ == "__main__":
    app.run(debug=True)