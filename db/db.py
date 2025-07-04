import pymysql
from pymysql.err import OperationalError
import os
from dotenv import load_dotenv


load_dotenv()

DB_CONFIG = {
        "host": os.getenv("DB_HOST"),
        "user": os.getenv("DB_USER"),
        "password": os.getenv("DB_PASSWORD"),
        "database": os.getenv("DB_NAME"),
        "port": int(os.getenv("DB_PORT", 3306)),
        "charset": "utf8mb4",
    }

def get_connection():

    try:
        conn = pymysql.connect(**DB_CONFIG)
        print('Connected to DB:', DB_CONFIG.get("database"))
        
        return conn
    except OperationalError as e:
        if e.args[0] == 1049:
            print(f"Database '{DB_CONFIG.get("database")}' does not exist. Creating it...")

            ## DB 없이 연결
            conn = pymysql.connect(
                host=DB_CONFIG.get("host"),
                user=DB_CONFIG.get("user"),
                passwd=DB_CONFIG.get("password"),
                charset=DB_CONFIG.get("charset")
            )
            with conn.cursor() as cursor:
                cursor.execute(f"CREATE DATABASE {DB_CONFIG.get("database")} DEFAULT CHARACTER SET {DB_CONFIG.get("charset")}")
                print(f"Database {DB_CONFIG.get("database")} created.")
            conn.select_db(DB_CONFIG.get("database"))
            return conn
    else:
        print("Connection failed:", e)
        raise



