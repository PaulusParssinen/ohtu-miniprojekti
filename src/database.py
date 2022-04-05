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
    
    def drop_tables_from_db(self):
        """Drops all tables from db.
        """

        db_cursor = self.connection.cursor()

        db_cursor.execute("DROP TABLE IF EXISTS ReadingTip")

        self.connection.commit()


    def ensure_tables_are_created(self):
        """Creates all tables to db if they do not already exist.
        """

        db_cursor = self.connection.cursor()

        db_cursor.execute("CREATE TABLE IF NOT EXISTS ReadingTip (\
            Id INTEGER PRIMARY KEY, \
            Title TEXT, \
            Author TEXT, \
            Type TEXT, \
            Isbn TEXT, \
            Url TEXT, \
            Description TEXT, \
            Comment TEXT)")
        self.connection.commit()
        
    def reset_database(self):
        """Drops database if it exists and creates new tables.
        """
        self.drop_tables_from_db()
        self.ensure_tables_are_created()
    
db = Database("readingtips.db")
