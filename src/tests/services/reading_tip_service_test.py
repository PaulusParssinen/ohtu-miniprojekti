import unittest

from database import Database

from entities.reading_tip import ReadingTip
from services.reading_tip_service import ReadingTipService
from repositories.reading_tip_repository import ReadingTipRepository

class TestReadingTipService(unittest.TestCase):
    def setUp(self):
        db = Database(":memory:")
        self.repository = ReadingTipRepository(db)
        tip = ReadingTip(
            title="Tirakirja",
            author="Laaksonen",
            url="https://www.cs.helsinki.fi/u/ahslaaks/tirakirja/",
            status="Not read yet!")
        self.repository.create(tip)
        self.service = ReadingTipService(self.repository)

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
    
    def test_get_unread_should_return_one_result(self):
        self.assertEqual(1, len(self.service.get_unread()))

    def test_delete_by_existing_id_should_work(self):
        self.service.delete(1)
        self.assertIsNone(self.service.get_by_id(1))

    def test_search_by_title_returns_false_if_not_found(self):
        self.assertEqual(0, len(self.service.search_by_title("Unknown")))

    def test_search_by_title_exact_returns_result(self):
        self.assertEqual(1, len(self.service.search_by_title("Tira")))

    def test_search_by_title_misspelled_returns_result(self):
        self.assertEqual(1, len(self.service.search_by_title("trakirja")))

    def test_get_with_existing_reading_tip(self):
        reading_tip = self.service.get_by_id(1)
        self.assertEqual(1, reading_tip.id)

    def test_get_with_nonexisting_reading_tip(self):
        self.assertIsNone(self.service.get_by_id(100))

    def test_updating_title_returns_correct_value(self):
        existing_tip = self.service.get_by_id(1)
        self.assertEqual(existing_tip.title, "Tirakirja")
        existing_tip.title = "Algorytmit"
        self.assertEqual(existing_tip.title, "Algorytmit")

    def test_updating_author_returns_correct_value(self):
        existing_tip = self.service.get_by_id(1)
        existing_tip.author = "A. Laaksonen"
        self.assertEqual(existing_tip.author, "A. Laaksonen")

    def test_updating_url_returns_correct_value(self):
        existing_tip = self.service.get_by_id(1)
        existing_tip.url = "https://github.com/hy-tira/tirakirja/raw/master/tirakirja.pdf"
        self.assertEqual(existing_tip.url, "https://github.com/hy-tira/tirakirja/raw/master/tirakirja.pdf")

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

    def test_raises_error_if_title_more_than_200_characters(self):
        tip = 'm'*201
        with self.assertRaises(Exception):
            self.service.create(tip)
    
    def test_get_ids_return_correct_ids(self):
        tip2 = ReadingTip(title="Kirja2", author="Author", url="Linkki")
        tip3 = ReadingTip(title="Kirja3", author="Author3", url="Linkki3")

        self.repository.create(tip2)
        self.repository.create(tip3)

        tips = self.service.get_all()
        self.assertEqual(self.service.get_ids(tips), [1, 2, 3])

        self.service.delete(2)
        tips = self.service.get_all()
        self.assertEqual(self.service.get_ids(tips), [1, 3])