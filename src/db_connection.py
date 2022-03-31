import sqlite3

db = sqlite3.connect("readingtips.db")

def get_db_connection():
    return db
