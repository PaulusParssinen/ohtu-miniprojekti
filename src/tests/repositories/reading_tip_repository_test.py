import unittest
from database import Database
from entities.reading_tip import ReadingTip
from repositories.reading_tip_repository import ReadingTipRepository

class TestReadingTipsRepository(unittest.TestCase):
    def setUp(self):
        self.db = Database(":memory:")
        self.repository = ReadingTipRepository(self.db)
        self.repository.create(ReadingTip(title="Kirja 1", author="Author 1", url="Link 1"))

    def test_create_tip_with_non_empty_values_works(self):
        self.assertEqual(self.repository.get_by_id(1).title, "Kirja 1")

    def test_create_tip_with_empty_title_should_return_false(self):
        self.assertFalse(self.repository.create(ReadingTip()))

    def test_get_by_id_by_id_that_does_not_exist_returns_none(self):
        self.assertIsNone(self.repository.get_by_id(1337))

    def test_empty_repository_get_all_returns_empty_array(self):
        empty_db = Database(':memory:')
        empty_repository = ReadingTipRepository(empty_db)
        self.assertEqual(len(empty_repository.get_all()), 0)

    def test_get_all_reading_tips_returns_one_tip_with_correct_values(self):
        all_tips = self.repository.get_all()

        self.assertEqual(len(all_tips), 1)
        self.assertEqual(all_tips[0].title, "Kirja 1")
        self.assertEqual(all_tips[0].author, "Author 1")
        self.assertEqual(all_tips[0].url, "Link 1")

    def test_get_all_reading_tips_returns_two_tips(self):
        self.repository.create(ReadingTip(title="Kirja 2", author="Author 2", url="Link 2"))

        all_tips = self.repository.get_all()

        self.assertEqual(len(all_tips), 2)
    
    def test_get_unread_reading_tips_returns_one_tip_with_correct_values(self):
        unread_tips = self.repository.get_unread()

        self.assertEqual(len(unread_tips), 1)
        self.assertEqual(unread_tips[0].title, "Kirja 1")
        self.assertEqual(unread_tips[0].author, "Author 1")
        self.assertEqual(unread_tips[0].url, "Link 1")

    def test_updating_with_valid_title_should_update_title_and_keep_other_fields_same(self):
        tip = self.repository.get_by_id(1)
        tip.title = "Valid Book Title"
        success = self.repository.update(tip)
        updated_tip = self.repository.get_by_id(1)

        self.assertTrue(success)
        self.assertEqual(updated_tip.title, "Valid Book Title")
        self.assertEqual(updated_tip.author, "Author 1")
        self.assertEqual(updated_tip.url, "Link 1")

    def test_updating_with_empty_title_should_return_false_and_not_update_any_fields(self):
        tip = self.repository.get_by_id(1)
        tip.title = ""
        success = self.repository.update(tip)

        updated_tip = self.repository.get_by_id(1)

        self.assertFalse(success)
        self.assertEqual(updated_tip.title, "Kirja 1")
        self.assertEqual(updated_tip.author, "Author 1")
        self.assertEqual(updated_tip.url, "Link 1")

    def test_deleting_tip_that_exists_works(self):
        self.repository.delete(1)
        self.assertIsNone(self.repository.get_by_id(1))
