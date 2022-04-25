from database import (db as default_tag_db)
from entities.tag import Tag


class TagsRepository:
    """All database operations related to Tags
    """

    def __init__(self, db=default_tag_db):
        self._db = db

    def create_tag(self, tag_name):
        """Inserting a new tag into Tags table.
        """

        db_cursor = self._db.connection.cursor()
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
        """Check if given tag name already exists in Tags table
        """

        db_cursor = self._db.connection.cursor()

        query_result = db_cursor.execute(
            "SELECT Tag_name FROM Tags WHERE Tag_name = ?", [tag_name]
        ).fetchone()

        if query_result is not None:
            return True
        return False

    def get_all_tags(self):
        """Returns all reading tips from Tags table
        """

        db_cursor = self._db.connection.cursor()

        query_result = db_cursor.execute(
            "SELECT Tag_name FROM Tags"
        ).fetchall()

        return self.create_tags_from_results(query_result)

    def get_tag_id(self, tag_name):
        """Returns tag_id by tag_name from Tags table
        """

        db_cursor = self._db.connection.cursor()

        query_result = db_cursor.execute(
            "SELECT Tag_Id FROM Tags WHERE Tag_name = ?", (tag_name, )
        ).fetchone()

        if query_result is None:
            return None
        return query_result[0]

    def get_tag_by_name(self, tag_name) -> Tag:
        """Returns tag_name based on tag_name
        """

        db_cursor = self._db.connection.cursor()

        query_result = db_cursor.execute(
            "SELECT Tag_name FROM Tags WHERE Tag_name=?", [tag_name]
        ).fetchone()

        return self.create_tag_from_result(query_result)

    def create_tag_from_result(self, result_row):
        """Transforms and returns query result to Tag object
        """

        return Tag(tag_name=result_row[0])

    def create_tags_from_results(self, result_row):
        """Creates and returns a list of Tag objects
        """

        tags = []
        for row in result_row:
            tags.append(self.create_tag_from_result(row))
        return tags

tags_repository = TagsRepository()
