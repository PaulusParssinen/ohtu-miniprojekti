from database import (db as default_reading_tip_db)
from entities.reading_tip import ReadingTip

class TagsRepository:
    """All database operations related to reading tips (adding, modifying and deleting)
    """

    def __init__(self, db=default_reading_tip_db):
        self._db = db

    def create_tag(self, reading_tip_object: ReadingTip):
        """Creates tags to the Tags table in database. """

        db_cursor = self._db.connection.cursor()

        tag_to_db = [
            reading_tip_object.tags
        ]
        try:
            db_cursor.execute("INSERT INTO Tags (Tag_id, Tag_name) VALUES (?)", tuple(tag_to_db))
            self._db.connection.commit()
        except:
            return False
        return True

    def get_tag_by_id(self, tag_id) -> ReadingTip:
        db_cursor = self._db.connection.cursor()

        query_result = db_cursor.execute(
            "SELECT * FROM Tags WHERE Id = ?", (tag_id,)
        ).fetchone()

        return self.create_tag_from_result(query_result)

    def insert_tag_into_reading_tip_repository(self):
        """Inserts wanted tags from Tags table into wanted reading tips in readingtip table"""
        db_cursor = self._db.connection.cursor()

        try:

            db_cursor.execute("INSERT INTO ReadingTip (Tags) SELECT Tag_name FROM Tags WHERE Tag_id=?)")
            self._db.connection.commit()
        except:
            return False
        return True

    def get_all_tags(self):
        pass

    def create_tag_from_result(self, result_row):

        if not result_row:
            return None
        return ReadingTip(tag=result_row[8])

    def create_tags_from_result(self, result_rows):
        tags = []
        for row in result_rows:
            tags.append(self.create_tip_from_result(row))
        return tags

tags_repository = TagsRepository()