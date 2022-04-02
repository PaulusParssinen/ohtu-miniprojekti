from entities.reading_tip import ReadingTip
from db_connection import get_db_connection


class ReadingTipRepository:
    """All database operations related to reading tips (adding, modifying and deleting)
    """
    
    
    def __init__(self, db_connection):
        """Initializing class with db connection as parameter.
        """
        
        self._db_connection = db_connection
    
    
    def create(self, reading_tip_object):
        """Inserting new reading tip into db.
        
           Data is checked before inserting into db:
           - None values are replaced with empty strings
           - Non-string values are replaced with strings
        """
        
        db_cursor = self._db_connection.cursor()
        
        values_to_db = [reading_tip_object.title, reading_tip_object.author, reading_tip_object.type, reading_tip_object.isbn, reading_tip_object.url, reading_tip_object.description, reading_tip_object.comment]
        
        # Data checked before inputting into db:
        for index, value in enumerate(values_to_db):
            if value == None:
                values_to_db[index] = ''
            elif not isinstance(value, str):
                values_to_db[index] = str(value)
        
        db_cursor.execute(
            "INSERT INTO ReadingTip (Title, Author, Type, Isbn, Url, Description, Comment) VALUES (?, ?, ?, ?, ?, ?, ?)", values_to_db
        )
        
        self._db_connection.commit()
    
    
    def delete(self, reading_tip_id):
        """Deleting existing reading tip from db.
        
            If reading tip with given id does not exist in the db, nothing is done.
        """
        
        db_cursor = self._db_connection.cursor()
        
        try:
            db_cursor.execute(
                "DELETE FROM ReadingTip WHERE Id = ?", [reading_tip_id]
            )
        except:
            pass
        
        self._db_connection.commit()



reading_tip_repository = ReadingTipRepository(get_db_connection())


