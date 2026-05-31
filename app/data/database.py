import sqlite3
import shutil

from app.utils.paths import data_path, fallback_data_path, seed_data_path


DATABASE_FILENAME = "Form1.db"
DATABASE_PATH = data_path(DATABASE_FILENAME)


def use_fallback_database():
    global DATABASE_PATH
    DATABASE_PATH = fallback_data_path(DATABASE_FILENAME)


def ensure_database():
    seed_path = seed_data_path("Form1.db")

    try:
        if DATABASE_PATH.exists():
            return
    except OSError:
        use_fallback_database()

        if DATABASE_PATH.exists():
            return

    if seed_path.exists():
        shutil.copy2(seed_path, DATABASE_PATH)


def get_connection():
    ensure_database()

    try:
        return sqlite3.connect(DATABASE_PATH)
    except sqlite3.Error:
        use_fallback_database()
        ensure_database()
        return sqlite3.connect(DATABASE_PATH)


def create_user_table():
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS user (
                fname TEXT,
                lname TEXT,
                email TEXT,
                gender TEXT,
                country TEXT,
                username TEXT UNIQUE,
                password TEXT
            )
        """)
        conn.commit()
    finally:
        conn.close()


def register_user(first_name, last_name, email, gender, country, username, password):
    create_user_table()
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO user
            (fname, lname, email, gender, country, username, password)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            first_name,
            last_name,
            email,
            gender,
            country,
            username,
            password,
        ))
        conn.commit()
    finally:
        conn.close()


def authenticate_user(username, password):
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM user WHERE username=? AND password=?",
            (username, password),
        )
        return cursor.fetchone()
    finally:
        conn.close()
