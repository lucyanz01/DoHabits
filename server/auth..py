import jwt 
import os
from datetime import datetime, timedelta
from flask import jsonify, request
from functools import wraps

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"