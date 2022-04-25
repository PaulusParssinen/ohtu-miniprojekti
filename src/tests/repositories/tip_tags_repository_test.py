import unittest
from database import Database

from entities.reading_tip import ReadingTip

from repositories.tags_repository import TagsRepository
from repositories.tip_tags_repository import TipTagsRepository
from repositories.reading_tip_repository import ReadingTipRepository


class TestTipTagsRepository(unittest.TestCase):
    def setUp(self):
        self.db = Database(":memory:")
        self.tip_tags_repository = TipTagsRepository(self.db)
        self.reading_tip_repository = ReadingTipRepository(self.db)
        self.reading_tip_repository.create(ReadingTip(title="Tirakirja"))
        self.tip_tags_repository.add_tag_to_reading_tip(1, 1)

    def test_add_tag_to_reading_tip_works(self):
        self.assertTrue(self.tip_tags_repository.add_tag_to_reading_tip(2, 2))
    
    def test_check_if_tag_added_to_tip_works(self):
        self.tip_tags_repository.add_tag_to_reading_tip(1, 1)
        self.assertTrue(self.tip_tags_repository.check_if_tag_added_to_tip(1, 1))
        self.assertFalse(self.tip_tags_repository.check_if_tag_added_to_tip(1, 10000))

    def test_get_all_tip_tag_pairs_works(self):
        tip_tag_pairs = self.tip_tags_repository.get_all_tip_tag_pairs()
        self.assertEqual(tip_tag_pairs, [(1, 1)])
    
    def test_get_all_reading_tips_with_tag_id(self):
        tip_tag_pairs = self.tip_tags_repository.get_all_reading_tip_ids_with_tag_id(1)
        self.assertEqual(tip_tag_pairs[0], 1)
        
        self.reading_tip_repository.create(ReadingTip(title="Competitive Programmer’s Handbook"))
        self.assertTrue(self.tip_tags_repository.add_tag_to_reading_tip(2, 1))

    def test_get_all_tag_ids_with_tip_id(self):
        tags_repository = TagsRepository(self.db)
        tags_repository.create_tag("Käpistely")
        tags_repository.create_tag("Algot")

        cses_book_tip = ReadingTip(title="Competitive Programmer’s Handbook")
        cses_book_id = self.reading_tip_repository.create(cses_book_tip)
        tags = self.tip_tags_repository.get_all_tag_ids_with_tip_id(cses_book_id)

        self.assertEqual(len(tags), 0)

        self.tip_tags_repository.add_tag_to_reading_tip(cses_book_id, 1)
        self.tip_tags_repository.add_tag_to_reading_tip(cses_book_id, 2)

        tags = self.tip_tags_repository.get_all_tag_ids_with_tip_id(cses_book_id)
        self.assertEqual(len(tags), 2)
