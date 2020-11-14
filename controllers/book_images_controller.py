from models.BookImage import BookImage
from models.Book import Book
from main import db
from pathlib import Path
import flask
from schemas.BookImageSchema import book_image_schema
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import Blueprint, request, jsonify, abort, send_from_directory
from services.auth_service import verify_user
import boto3

book_images = Blueprint("book_images", __name__, url_prefix="/books/<int:book_id>/image")

@book_images.route("/", methods=["POST"])
@jwt_required
@verify_user
def book_image_create(book_id, user=None):
    book = Book.query.filter_by(id=book_id, user_id=get_jwt_identity()).first()
    
    if not book:
        return abort(401, description="unauthorized")
    
    if "image" not in request.files:
        return abort(401, description="No image")
        
    image = request.files["image"]
        
    if Path(image.filename).suffix not in {".png", ".jpg", ".jpeg"}:
        return abort(401, description="not a png")
    
    filename = f"{book_id}{Path(image.filename).suffix}"
    bucket = boto3.resource("s3").Bucket(flask.current_app.config["AWS_S3_BUCKET"])
    
    key = f"book_image/{filename}"
    
    bucket.upload_fileobj(image, key)
    
    if not(book.book_image):
        new_image = BookImage()
        new_image.filename = filename 
        book.book_image = new_image
        db.session.commit()
    
    return ("", 200)

@book_images.route("/", methods=["GET"])
def book_image_show(book_id, user=None):
    book_image = BookImage.query.filter_by(book_id=book_id).first()
    if not book_image:
        return abort(404, "No image")
    
    bucket = boto3.resource("s3").Bucket(flask.current_app.config["AWS_S3_BUCKET"])
    
    filename = book_image.filename
    
    file_obj = bucket.Object(f"book_image/{filename}").get()
    
    return flask.Response(
        file_obj["Body"].read(),
        mimetype="image/*",
        headers={"Content-Disposition": "attachment;filename=image"}
    )

@book_images.route("/", methods=["DELETE"])
@jwt_required
def book_image_delete(book_id, user=None):
    return "3"