from database import (db as default_tag_db)
from entities.tag import Tag


class TagsRepository:
    """All database operations related to Tags
    """

    def __init__(self, db=default_tag_db):
        self._db = db

    def create_tag(self, tag_name):
        """Inserting a new tag into Tags table."""

        db_cursor = self._db.connection.cursor()
        try:
            db_cursor.execute(
                    "INSERT INTO Tags (Tag_name) \
                    VALUES (?)", (Tag(tag_name), )
                    )
            self._db.connection.commit()
        except:
            return False
        return True

    def get_all_tags(self):
        """Returns all reading tips from db.
        """

        db_cursor = self._db.connection.cursor()

        query_result = db_cursor.execute(
            "SELECT * FROM Tags"
        ).fetchall()

        return self.create_tips_from_results(query_result)

    def get_by_tag_name(self, tag_name):
        db_cursor = self._db.connection.cursor()

        query_result = db_cursor.execute(
            "SELECT * FROM Tags WHERE Tag_name = ?", (tag_name,)
        ).fetchone()

        return self.create_tag_from_result(query_result)

    def create_tag_from_result(self, result_row):
        return Tag(result_row)

    def create_tags_from_result(self, result_row):
        tags = []
        for row in result_row:
            tags.append(self.create_tip_from_result(row))
        return tags

tags_repository = TagsRepository()