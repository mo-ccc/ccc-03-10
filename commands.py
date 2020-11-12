from main import db
from flask import Blueprint

db_commands = Blueprint("db", __name__)

@db_commands.cli.command("Wisdom")
def wisdom():
    print("Hello World!")
    
@db_commands.cli.command("create")
def create_db():
    db.create_all()
    print("tables created")

@db_commands.cli.command("drop")
def drop_db():
    db.drop_all()
    print("tables dropped")
    
@db_commands.cli.command("seed")
def seed_db():
    from models.Book import Book
    from faker import Faker
    faker = Faker()
    for i in range(10):
        book = Book()
        book.title = faker.catch_phrase()
        db.session.add(book)
    db.session.commit()
    print("Tables seeded")
    