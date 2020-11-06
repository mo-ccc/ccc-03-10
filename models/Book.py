from main import db

# A book model
class Book(db.Model):
    __tablename__ = "books"
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String())