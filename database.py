import psycopg2
import dotenv
import os

dotenv.load_dotenv()

connection = psycopg2.connect(
    database=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASS"),
    host=os.getenv("HOST")
)

cursor = connection.cursor()