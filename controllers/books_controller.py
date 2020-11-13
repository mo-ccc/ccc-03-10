from models.Book import Book
from schemas.BookSchema import book_schema, books_schema
from main import db
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required

# books route set with a url prefix of /books
books = Blueprint('books', __name__, url_prefix="/books")

@books.route("/", methods=["GET"])
def book_index():
    # Return all books
    books = Book.query.all()
    return jsonify(books_schema.dump(books))

@books.route("/", methods=["POST"])
@jwt_required
def book_create():
    # Create a new book
    data = book_schema.load(request.json)
    
    new_book = Book()
    new_book.title = data["title"]
    
    db.session.add(new_book)
    db.session.commit()
    
    return jsonify(books_schema.dump(Book.query.all()))

@books.route("/<int:id>", methods=["GET"])
def book_show(id):
    # Return a single book
    book = Book.query.get(id)
    return jsonify(book_schema.dump(book))

@books.route("/<int:id>", methods=["PUT", "PATCH"])
@jwt_required
def book_update(id):
    # Update a book
    data = book_schema.load(request.json)
    book = Book.query.get(id)
    book.title = data["title"]
    db.session.commit()
    return jsonify(books_schema.dump(Book.query.all()))
    

@books.route("/<int:id>", methods=["DELETE"])
def book_delete(id):
    # Delete a book
    book = Book.query.get(id)
    db.session.delete(book)
    db.session.commit()
    return jsonify(books_schema.dump(Book.query.all()))