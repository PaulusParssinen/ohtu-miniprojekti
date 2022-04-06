import unittest

from database import Database

from entities.reading_tip import ReadingTip
from services.reading_tip_service import ReadingTipService
from repositories.reading_tip_repository import ReadingTipRepository

class TestReadingTipService(unittest.TestCase):
    def setUp(self):
        db = Database(":memory:")
        repository = ReadingTipRepository(db)
        
        tip = ReadingTip(
            title="Tirakirja", 
            author="Laaksonen", 
            url="https://www.cs.helsinki.fi/u/ahslaaks/tirakirja/")
        repository.create(tip)
        self.service = ReadingTipService(repository)

    def test_create_with_valid_title_should_add_a_new_tip(self):
        self.service.create("Kirja")
        added_tip = self.service.get_by_id(2)
        
        self.assertEqual("Kirja", added_tip.title)

    def test_create_with_empty_title_should_raise_error_and_not_add_new_tip(self):
        with self.assertRaises(Exception):
            self.service.create("")
        
        self.assertIsNone(self.service.get_by_id(2))
        
    def test_get_all_should_return_one_result(self):
        self.assertEqual(1, len(self.service.get_all()))

    def test_delete_by_existing_id_should_work(self):
        self.service.delete(1)
        self.assertIsNone(self.service.get_by_id(1))

    def test_search_by_title_returns_false_if_not_found(self):
        self.assertFalse(self.service.search_by_title("Unknown"))
    
    def test_search_by_title_returns_true_if_found(self):
        self.assertEqual(1, len(self.service.search_by_title("Tira")))

    def test_get_with_existing_reading_tip(self):
        reading_tip = self.service.get_by_id(1)
        self.assertEqual(1, reading_tip.id)

    def test_get_with_nonexisting_reading_tip(self):
        self.assertIsNone(self.service.get_by_id(100))

    def test_update_by_tip_id(self):
        self.service.update_by_id(1, 'Muutettu Kirja 1')
        reading_tip = self.service.get_by_id(1)

        self.assertEqual(reading_tip.title, 'Muutettu Kirja 1')

    def test_update_nonexistent_id_should_raise_error(self):
        with self.assertRaises(Exception):
            self.service.update_by_id(1337)
    
    def test_updating_author_and_link_of_existing_reading_tip_should_work(self):
        existing_tip = self.service.get_by_id(1)
        
        existing_tip.author = "A. Laaksonen"
        existing_tip.url = "https://github.com/hy-tira/tirakirja/raw/master/tirakirja.pdf"
        
        self.service.update(existing_tip)
        updated_tip = self.service.get_by_id(1)
        
        self.assertEqual(updated_tip.title, "Tirakirja")
        self.assertEqual(updated_tip.author, "A. Laaksonen")
        self.assertEqual(updated_tip.url, 
            "https://github.com/hy-tira/tirakirja/raw/master/tirakirja.pdf")
    
    def test_updating_with_empty_title_should_raise_error(self):
        existing_tip = self.service.get_by_id(1)
        
        existing_tip.title = ""
        existing_tip.author = "A. Laaksonen"
        existing_tip.url = "https://github.com/hy-tira/tirakirja/raw/master/tirakirja.pdf"
        
        with self.assertRaises(Exception):
            self.service.update(existing_tip)
    
    def test_updating_nonexistent_tip_should_return_false(self):
        nonexistent_tip = ReadingTip(1337, "This tip should not exist")
        
        self.assertFalse(self.service.update(nonexistent_tip))
