# __init__.py
from flask import Flask
app = Flask(__name__)
app.secret_key = "shhhhhh"

MyCustomDB = 'users_and_cars_schema'