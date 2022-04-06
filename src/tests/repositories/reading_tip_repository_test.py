import unittest

from database import Database

from entities.reading_tip import ReadingTip
from repositories.reading_tip_repository import ReadingTipRepository

class TestReadingTipsRepository(unittest.TestCase):
    def setUp(self):
        db = Database(":memory:")
        self.repository = ReadingTipRepository(db)
    
    def test_create_tip_with_non_empty_values_works(self):
        self.repository.create(ReadingTip(title="Kirja 1", author="Author 1", url="Link 1"))
        self.repository.get_by_id(0)
    
    def test_get_all_reading_tips_returns_one_tip_with_correct_title(self):
        self.repository.create(ReadingTip(title="Kirja 1", author="Author 1", url="Link 1"))
        
        all_tips = self.repository.get_all()
        self.assertEqual(len(all_tips), 1)
        self.assertEqual(all_tips[0].title, "Kirja 1")
        
    def test_get_all_reading_tips_returns_two_tips(self):
        self.repository.create(ReadingTip(title="Kirja 1", author="Author 1", url="Link 1"))
        self.repository.create(ReadingTip(title="Kirja 2", author="Author 2", url="Link 2"))
        
        all_tips = self.repository.get_all()
        self.assertEqual(len(all_tips), 2)