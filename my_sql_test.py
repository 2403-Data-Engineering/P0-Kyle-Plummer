import os
import mysql.connector

from dotenv import load_dotenv


load_dotenv()
conn = mysql.connector.connect(
    host=os.getenv("host"),
    port=3306,
    user=os.getenv("user"),
    password=os.getenv("pass"),
    database="your_database"
)