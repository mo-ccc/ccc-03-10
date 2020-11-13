from models.Book import Book
from models.User import User
from schemas.BookSchema import book_schema, books_schema
from main import db
from flask import Blueprint, request, jsonify, abort
import flask_jwt_extended
from services.auth_service import verify_user
from sqlalchemy.orm import joinedload

# books route set with a url prefix of /books
books = Blueprint('books', __name__, url_prefix="/books")

@books.route("/", methods=["GET"])
def book_index():
    # Return all books
    books = Book.query.options(joinedload("user")).all()
    return jsonify(books_schema.dump(books))

@books.route("/", methods=["POST"])
@flask_jwt_extended.jwt_required
def book_create(user=None):
    # Create a new book
    data = book_schema.load(request.json)
    new_book = Book()
    new_book.title = data["title"]
    
    user.books.append(new_book)
    db.session.commit()
    
    return jsonify(books_schema.dump(Book.query.all()))

@books.route("/<int:id>", methods=["GET"])
def book_show(id):
    # Return a single book
    book = Book.query.get(id)
    return jsonify(book_schema.dump(book))

@books.route("/<int:id>", methods=["PUT", "PATCH"])
@flask_jwt_extended.jwt_required
@verify_user
def book_update(id, user=None):
    # Update a book
    
    data = book_schema.load(request.json)
    book = Book.query.filter_by(id=id, user_id=user.id).first()
    
    if not book:
        return abort(401, description="Unauthorized request")
    
    book.title = data["title"]
    db.session.commit()
    return jsonify(books_schema.dump(Book.query.all()))
    
@books.route("/<int:id>", methods=["DELETE"])
@flask_jwt_extended.jwt_required
@verify_user
def book_delete(id, user=None):
    # Delete a book
    book = Book.query.filter_by(id=id, user_id=user.id).first()
    
    if not book:
        return abort(401, description="Unauthorized request")
        
    db.session.delete(book)
    db.session.commit()
    return jsonify(books_schema.dump(Book.query.all()))