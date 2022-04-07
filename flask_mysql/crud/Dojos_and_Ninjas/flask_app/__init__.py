# __init__.py
from flask import Flask
app = Flask(__name__)
app.secret_key = "shhhhhh"          #<-- literally anything

MyCustomDB = 'dojos_and_ninjas_schema'         #<-- reference source for the name of the current database all model files can use