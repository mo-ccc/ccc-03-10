from flask import Flask, request, jsonify, abort
from database import init_db
import os


app = Flask(__name__)
db = init_db(app)

from controllers import registerable_controllers

for controller in registerable_controllers:
    app.register_blueprint(controller)
