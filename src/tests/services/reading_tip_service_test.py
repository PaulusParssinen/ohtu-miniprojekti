import unittest

from database import Database

from entities.reading_tip import ReadingTip
from services.reading_tip_service import ReadingTipService
from repositories.reading_tip_repository import ReadingTipRepository

class TestReadingTipService(unittest.TestCase):
    def setUp(self):
        db = Database(":memory:")
        self.repository = ReadingTipRepository(db)

        self._reading_tip_service = ReadingTipService(self.repository)

        reading_tip1 = ReadingTip(title="Kirja 1", author="Author 1", url="Link 1")
        self.repository.create(reading_tip1)

    def test_search_by_title_returns_false_if_not_found(self):
        self.assertFalse(self._reading_tip_service.search_reading_tip_by_title("Unknown"))
    
    def test_search_by_title_returns_true_if_found(self):
        self.assertTrue(self._reading_tip_service.search_reading_tip_by_title("Kirja 1"))

    def test_get_reading_tip_with_existing_reading_tip(self):
        reading_tip = self._reading_tip_service.get_reading_tip_by_id(1)
        self.assertEqual(1, reading_tip.id)

    def test_get_reading_tip_with_nonexisting_reading_tip(self):
        self.assertEqual(None, self._reading_tip_service.get_reading_tip_by_id(100))

    def test_modify_reading_tip_by_tip_id(self):
        self._reading_tip_service.modify_reading_tip_by_id(1, 'Muutettu Kirja 1')
        reading_tip = self._reading_tip_service.get_reading_tip_by_id(1)

        self.assertEqual(reading_tip.title, 'Muutettu Kirja 1')
