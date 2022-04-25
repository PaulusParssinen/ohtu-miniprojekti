from database import (db as default_tip_tag_db)

class TipTagsRepository:
    """All database operations related to TipTags table
    """

    def __init__(self, db=default_tip_tag_db):
        self._db = db

    def add_tag_to_reading_tip(self, tip_id, tag_id):
        """Inserting a new tip-tag pair into TipTags table"""

        db_cursor = self._db.connection.cursor()
        try:
            db_cursor.execute(
                    "INSERT INTO TipTags (Tip_id, Tag_Id) \
                    VALUES (?, ?)", (tip_id, tag_id)
                    )
            self._db.connection.commit()
        except:
            return False
        return True
    
    def check_if_tag_added_to_tip(self, tip_id, tag_id):
        """Checks if tag is already added to the tip."""
        
        db_cursor = self._db.connection.cursor()
        
        query_result = db_cursor.execute(
            "SELECT * FROM TipTags WHERE Tip_Id=? AND Tag_Id=?", (tip_id, tag_id)
        ).fetchone()
        
        if query_result is None:
            return False

        return True
    
    def get_all_tip_tag_pairs(self):
        """Returns all tip-tags pairs from the database."""
        
        db_cursor = self._db.connection.cursor()
        
        query_result = db_cursor.execute(
            "SELECT * FROM TipTags"
        ).fetchall()

        return query_result
    
    def get_all_reading_tip_ids_with_tag_id(self, tag_id):
        """Returns all reading ids of the tips that have given tag id linked to it."""
        
        db_cursor = self._db.connection.cursor()
        
        pairs = db_cursor.execute(
            "SELECT * FROM TipTags WHERE Tag_id=?", (tag_id,)
        ).fetchall()
        
        tip_ids = []
        for pair in pairs:
            tip_ids.append(pair[0])
        
        return tip_ids

    def get_all_tag_ids_with_tip_id(self, tip_id):
        """Returns all tag ids linked to given tip id from the database."""
        
        db_cursor = self._db.connection.cursor()
        
        query_result = db_cursor.execute(
            "SELECT Tag_id FROM TipTags WHERE Tip_id=?", (tip_id,)
        ).fetchall()
        
        tag_ids = []
        for pair in query_result:
            tag_ids.append(pair[0])
        return tag_ids

tip_tags_repository = TipTagsRepository()
