from main import db
from flask import Blueprint
import random
from main import bcrypt

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
    from models.User import User
    from faker import Faker
    faker = Faker()
    array = []
    for i in range(5):
        user = User()
        user.email = f"test{i}@test.com"
        user.password = bcrypt.generate_password_hash("12345678").decode("utf-8")
        array.append(user)
        db.session.add(user)
    db.session.commit()
    
    for i in range(10):
        book = Book()
        book.title = faker.catch_phrase()
        book.user_id = random.choice(array).id
        db.session.add(book)
    db.session.commit()
    print("Tables seeded")
    