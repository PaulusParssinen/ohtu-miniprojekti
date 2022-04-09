
from database import db

def pytest_configure():
    """Alustaa tietokannan testejä varten"""
    db.drop_tables_from_db()
    db.reset_database()