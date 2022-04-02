from db_connection import get_db_connection

class ReadingTipRepository:
    """A class that represents the SQL reading tip queries."""
    def __init__(self):
        self._connection = get_db_connection()

    def delete(self, tip_id):
        cursor = self._connection.cursor()
        cursor.execute("DELETE FROM ReadingTip WHERE id=?", tip_id)
        self._connection.commit()
