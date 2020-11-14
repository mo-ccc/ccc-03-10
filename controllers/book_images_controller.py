from models.BookImage import BookImage
from models.Book import Book
from schemas.BookImageSchema import book_image_schema
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import Blueprint, request, jsonify, abort
from services.auth_service import verify_user

book_images = Blueprint("book_images", __name__, url_prefix="/books/<int:book_id>/image")

@book_images.route("/", methods=["POST"])
@jwt_required
@verify_user
def book_image_create(book_id, user=None):
    return "1"

@book_images.route("/<int:id>", methods=["GET"])
@jwt_required
@verify_user
def book_image_show(book_id, id, user=None):
    return "2"

@book_images.route("/<int:id>", methods=["DELETE"])
@jwt_required
def book_image_delete(book_id, id, user=None):
    return "3"