from thefuzz import fuzz
from database import (db as default_reading_tip_db)
from entities.reading_tip import ReadingTip

class ReadingTipRepository:
    """All database operations related to reading tips (adding, modifying and deleting)
    """

    def __init__(self, db=default_reading_tip_db):
        """Initializing class with db connection as parameter.
        """
        self._db = db

    def create(self, reading_tip_object: ReadingTip) -> bool:
        """Inserting new reading tip into db.

           If the given ReadingTip was successfully inserted into the database, returns row number.
           If the given ReadingTip does not follow the database schema constraints; returns False.
        """

        db_cursor = self._db.connection.cursor()

        values_to_db = [
            reading_tip_object.title,
            reading_tip_object.author,
            reading_tip_object.type,
            reading_tip_object.isbn,
            reading_tip_object.url,
            reading_tip_object.description,
            reading_tip_object.comment,
            reading_tip_object.status
        ]
        try:
            db_cursor.execute(
                "INSERT INTO ReadingTip (Title, Author, Type, Isbn, \
                                        Url, Description, Comment, Status) \
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)", tuple(values_to_db)
            )
            self._db.connection.commit()
        except:
            return False
        return db_cursor.lastrowid

    def get_by_id(self, reading_tip_id) -> ReadingTip:
        """Returns reading tip based on given id from db.

           If reading tip on given id does not exist in the db, returns None.
        """

        db_cursor = self._db.connection.cursor()

        query_result = db_cursor.execute(
            "SELECT * FROM ReadingTip WHERE Tip_Id = ?", (reading_tip_id,)
        ).fetchone()

        return self.create_tip_from_result(query_result)

    def search_by_title(self, query) -> ReadingTip:
        """Returns reading tips that contain title similar to given query from db.
        """
        min_ratio = 80
        results = []
        for tip in self.get_all():
            if fuzz.WRatio(query, tip.title) >= min_ratio:
                results.append(tip)

        return results


    def get_all(self):
        """Returns all reading tips from db.
        """

        db_cursor = self._db.connection.cursor()

        query_result = db_cursor.execute(
            "SELECT * FROM ReadingTip"
        ).fetchall()

        return self.create_tips_from_results(query_result)

    def update(self, new_reading_tip):
        """Update existing ReadingTip in the database.
            If given ReadingTip was updated successfully, returns True.
            If the given ReadingTip does not follow the database schema constraints; returns False.
        """

        db_cursor = self._db.connection.cursor()

        values_to_db = [
            new_reading_tip.title,
            new_reading_tip.author,
            new_reading_tip.type,
            new_reading_tip.isbn,
            new_reading_tip.url,
            new_reading_tip.description,
            new_reading_tip.comment,
            new_reading_tip.id
            ]
        try:
            db_cursor.execute(
                "UPDATE ReadingTip SET \
                    Title=?, \
                    Author=?, \
                    Type=?, \
                    Isbn=?, \
                    Url=?, \
                    Description=?, \
                    Comment=? \
                    WHERE Tip_Id=?", tuple(values_to_db)
                )

            self._db.connection.commit()
        except:
            return False
        return True

    def update_status(self, new_reading_tip_status):

        db_cursor = self._db.connection.cursor()

        values_to_db = [
            new_reading_tip_status.status,
            new_reading_tip_status.id,
        ]

        try:
            db_cursor.execute(
                "UPDATE ReadingTip SET \
                    Status=? \
                    WHERE Tip_Id=?", tuple(values_to_db)
                )

            self._db.connection.commit()
        except:
            return False
        return True

    def delete(self, reading_tip_id) -> bool:
        """Deleting existing reading tip from db.
        """

        db_cursor = self._db.connection.cursor()
        db_cursor.execute(
            "DELETE FROM ReadingTip WHERE Tip_Id = ?", (reading_tip_id,)
        )

        self._db.connection.commit()

    def create_tip_from_result(self, result_row) -> ReadingTip:
        """Populates a ReadingTip object from a single query result row.

           If the the result row is empty, returns None.
        """
        if not result_row:
            return None

        return ReadingTip(
            identifier=int(result_row[0]),
            title=result_row[1],
            author=result_row[2],
            reading_type=result_row[3],
            isbn=result_row[4],
            url=result_row[5],
            description=result_row[6],
            comment=result_row[7],
            status=result_row[9]
        )


    def create_tips_from_results(self, result_rows):
        """Populates a list of ReadingTip object from query result rows.
           If result_rows is empty, returns None.
        """
        tips = []
        for row in result_rows:
            tips.append(self.create_tip_from_result(row))
        return tips

reading_tip_repository = ReadingTipRepository()
