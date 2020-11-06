from flask import Flask, request, jsonify, abort
from database import cursor, connection
import os
from controllers import registerable_controllers

app = Flask(__name__)

for controller in registerable_controllers:
    app.register_blueprint(controller)

cursor.execute("create table if not exists books (id serial PRIMARY KEY, title varchar);")
connection.commit()


