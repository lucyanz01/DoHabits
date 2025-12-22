from flask import Flask
from config import engine
from models import Base
from backend.routes.auth import bp as auth_bp
from backend.routes.dohabits_api import bp as api_bp

app = Flask(__name__)

