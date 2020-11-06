from database import cursor, connection
from flask import Blueprint, request, jsonify
authors = Blueprint('authors', __name__, url_prefix="/authors")

@authors.route("/", methods=["GET"])
def book_index():
    #Return all books
    sql = "SELECT * FROM authors"
    cursor.execute(sql)
    authors = cursor.fetchall()
    return jsonify(authors)