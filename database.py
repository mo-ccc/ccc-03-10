from flask_sqlalchemy import SQLAlchemy
import dotenv
import os

dotenv.load_dotenv()
def init_db(app):
    db = SQLAlchemy(app)
    return db