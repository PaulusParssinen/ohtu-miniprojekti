import sqlite3

db = sqlite3.connect("readingtips.db")

def get_db_connection():
    return db

def get_db_connection_for_testing():
    db_test = sqlite3.connect("test_readingtips.db")
    return db_test 
