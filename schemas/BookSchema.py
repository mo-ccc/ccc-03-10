from main import ma
from models.Book import Book
from marshmallow.validate import Length
from schemas.UserSchema import user_schema

class BookSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Book
    title = ma.String(required=True, validate=Length(min=1))
    user = ma.Nested(user_schema)

book_schema = BookSchema()
books_schema = BookSchema(many=True)