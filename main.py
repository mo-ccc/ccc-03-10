from flask import Flask, request, jsonify, abort
from database import cursor, connection
import os
from books import books

app = Flask(__name__)

app.register_blueprint(books)

cursor.execute("create table if not exists books (id serial PRIMARY KEY, title varchar);")
connection.commit()

