from database import (db as default_tip_tag_db)

class TipTagsRepository:
    """All database operations related to TipTags table
    """

    def __init__(self, db=default_tip_tag_db):
        self._db = db

    def add_tag_to_reading_tip(self, tip_id, tag_id):
        """Inserting a new tip-tag pair into TipTags table."""

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
    
    def get_all_reading_tips_with_tag_id(self, tag_id):
        """Returns all tip-tags pairs from the database with given tag_id."""
        
        db_cursor = self._db.connection.cursor()
        
        query_result = db_cursor.execute(
            "SELECT * FROM TipTags WHERE Tag_id=?", (tag_id,)
        ).fetchall()
        
        reading_tips = []
        
        for pair in query_result:
            tip_id, tag_id = pair
            reading_tip = db_cursor.execute(
                "SELECT * FROM ReadingTip WHERE Tip_Id=?", (tip_id,)
            ).fetchone()
            reading_tips.append(reading_tip)
        
        return reading_tips

tip_tags_repository = TipTagsRepository()
