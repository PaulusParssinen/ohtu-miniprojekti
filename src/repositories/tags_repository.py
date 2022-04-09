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

        # Check that given tag does not exist in the database already
        if self.check_if_tag_exists(tag_name):
            return False

        try:
            db_cursor.execute(
                    "INSERT INTO Tags (Tag_name) \
                    VALUES (?)", [tag_name]
                    )
            self._db.connection.commit()
        except:
            return False
        return True

    def check_if_tag_exists(self, tag_name):
        """Check if given tag name already exists in the database.
        """
        db_cursor = self._db.connection.cursor()

        query_result = db_cursor.execute(
            "SELECT Tag_name FROM Tags WHERE Tag_name = ?", [tag_name]
        ).fetchone()

        if query_result != None:
            return True
        else:
            return False

    def get_all_tags(self):
        """Returns all reading tips from db.
        """

        db_cursor = self._db.connection.cursor()

        query_result = db_cursor.execute(
            "SELECT * FROM Tags"
        ).fetchall()

        return self.create_tags_from_results(query_result)

    def get_tag_id(self, tag_name):
        db_cursor = self._db.connection.cursor()

        query_result = db_cursor.execute(
            "SELECT Tag_Id FROM Tags WHERE Tag_name = ?", (tag_name, )
        ).fetchone()

        if query_result is None:
            return None
        else:
            return query_result[0]
    
    def get_tag_by_name(self, tag_name) -> Tag:

        db_cursor = self._db.connection.cursor()

        query_result = db_cursor.execute(
            "SELECT Tag_name FROM Tags WHERE Tag_name=?", [tag_name]
        ).fetchone()

        return self.create_tag_from_result(query_result)

    def create_tag_from_result(self, result_row):
        return Tag(result_row[0])

    def create_tags_from_results(self, result_row):
        tags = []
        for row in result_row:
            tags.append(self.create_tag_from_result(row))
        return tags

tags_repository = TagsRepository()