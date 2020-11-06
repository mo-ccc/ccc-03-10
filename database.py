from flask_sqlalchemy import SQLAlchemy
import dotenv
import os

dotenv.load_dotenv()
def init_db(app):
    app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql+psycopg2://{os.getenv('DB_NAME')}:{os.getenv('DB_PASS')}@{os.getenv('HOST')}:5432/{os.getenv('DB_NAME')}"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db = SQLAlchemy(app)
    return db

# import psycopg2

# connection = psycopg2.connect(
#     database=os.getenv("DB_NAME"),
#     user=os.getenv("DB_USER"),
#     password=os.getenv("DB_PASS"),
#     host=os.getenv("HOST")
# )

# cursor = connection.cursor()