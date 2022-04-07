import sqlite3

class Database:
    """Class responsible for creating and initializing the database connection.
    """

    def __init__(self, file_name):
        """Opens a connection to the specified local database and ensures that
           the database tables are created.
        """
        self.connection = sqlite3.connect(file_name)
        self.ensure_tables_are_created()
        self.ensure_tags_table_is_created()
        self.ensure_tag_tips_table_is_created()

    def drop_tables_from_db(self):
        """Drops all tables from db.
        """

        db_cursor = self.connection.cursor()
        db_cursor.execute("DROP TABLE IF EXISTS ReadingTip")
        db_cursor.execute("DROP TABLE IF EXISTS Tags")
        db_cursor.execute("DROP TABLE IF EXISTS TagTips")

        self.connection.commit()


    def ensure_tables_are_created(self):
        """Creates all tables to db if they do not already exist.
        """

        db_cursor = self.connection.cursor()

        db_cursor.execute("CREATE TABLE IF NOT EXISTS ReadingTip (\
            Tip_Id INTEGER PRIMARY KEY, \
            Title TEXT CHECK(Title IS NOT NULL AND length(Title) > 0), \
            Author TEXT, \
            Type TEXT, \
            Isbn TEXT, \
            Url TEXT, \
            Description TEXT, \
            Comment TEXT, \
            Tags TEXT)")
        self.connection.commit()

    def ensure_tags_table_is_created(self):
        db_cursor = self.connection.cursor()

        db_cursor.execute("CREATE TABLE IF NOT EXISTS Tags (\
            Tag_Id INTEGER PRIMARY KEY, \
            Tag_name TEXT CHECK(Tag_name IS NOT NULL AND length(Tag_name) > 0))")
        self.connection.commit()

    def ensure_tag_tips_table_is_created(self):
        db_cursor = self.connection.cursor()

        db_cursor.execute("CREATE TABLE IF NOT EXISTS TagTips (\
            Tip_Id INTEGER REFERENCES ReadingTip, \
            Tag_Id INTEGER REFERENCES Tags)")
        self.connection.commit()

    def reset_database(self):
        """Drops database if it exists and creates new tables.
        """
        self.drop_tables_from_db()
        self.ensure_tables_are_created()
        self.ensure_tags_table_is_created()
        self.ensure_tag_tips_table_is_created()

db = Database("readingtips.db")
