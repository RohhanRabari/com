from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')  # Assuming your database configuration is in config.py
db = SQLAlchemy(app)

from app import views, models