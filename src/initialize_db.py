from db_connection import get_db_connection


def drop_tables_from_db(db_connection):
    """Drops all tables from db.
    """

    db_cursor = db_connection.cursor()

    db_cursor.execute("DROP TABLE IF EXISTS ReadingTip")

    db_connection.commit()


def create_tables_to_db(db_connection):
    """Creates all tables to db.
    """

    db_cursor = db_connection.cursor()

    db_cursor.execute("CREATE TABLE ReadingTip (\
        Id SERIAL PRIMARY KEY, \
        Title TEXT, Author TEXT, \
        Type TEXT, \
        Isbn TEXT, \
        Url TEXT, \
        Description TEXT, \
        Comment TEXT)")

    db_connection.commit()


def initialize_db():
    """Drops all tables from db and creates all the same tables again.
    """

    db_connection = get_db_connection()

    drop_tables_from_db(db_connection)
    create_tables_to_db(db_connection)


if __name__ == '__main__':
    initialize_db()
