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

    def test_check_reading_tip_with_existing_reading_tip(self):
        reading_tip = self._reading_tip_service.check_reading_tip_by_id(1)
        self.assertEqual(1, reading_tip[0])

    def test_check_reading_tip_with_nonexisting_reading_tip(self):
        self.assertEqual(False, self._reading_tip_service.check_reading_tip_by_id(100))

    def test_modify_reading_tip_by_tip_id(self):
        self._reading_tip_service.modify_reading_tip(1, 'Muutettu Kirja 1')
        reading_tip = self._reading_tip_service.check_reading_tip_by_id(1)

        self.assertEqual(reading_tip[1], 'Muutettu Kirja 1')
