import unittest
from entities.reading_tip import ReadingTip
from repositories.reading_tip_repository import ReadingTipRepository
from services.reading_tip_service import ReadingTipService
from db_connection import get_db_connection

class TestReadingTipService(unittest.TestCase):
    def setUp(self):
        self.repository = ReadingTipRepository(get_db_connection())

        self._reading_tip_service = ReadingTipService(self.repository)

        reading_tip1 = ReadingTip(title="Kirja 1", author="Author 1", url="Link 1")
        self.repository.create(reading_tip1)

    def test_search_by_title_returns_false_if_not_found(self):
        self.assertFalse(self._reading_tip_service.search_reading_tip_by_title("Unknown"))
    
    def test_search_by_title_returns_true_if_found(self):
        self.assertTrue(self._reading_tip_service.search_reading_tip_by_title("Kirja 1"))
    