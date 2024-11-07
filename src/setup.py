
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from os import getenv

load_dotenv()

secret_key = getenv("SECRET_KEY")
test_env = getenv("TEST_ENV") == "True"
print(f"Test environment: {test_env}")

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")
db = SQLAlchemy(app)
