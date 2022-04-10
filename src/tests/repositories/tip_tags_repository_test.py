import unittest
from database import Database
from entities.tag import Tag
from entities.reading_tip import ReadingTip
from repositories.tip_tags_repository import TipTagsRepository
from repositories.reading_tip_repository import ReadingTipRepository


class TestTipTagsRepository(unittest.TestCase):
    def setUp(self):
        self.db = Database(":memory:")
        self.tip_tags_repository = TipTagsRepository(self.db)
        self.reading_tip_repository = ReadingTipRepository(self.db)
        self.reading_tip_repository.create(ReadingTip(title="Kirja 1", author="Author 1", url="Link 1"))
        self.tip_tags_repository.add_tag_to_reading_tip(1,1)

    def test_add_tag_to_reading_tip_works(self):
        self.assertTrue(self.tip_tags_repository.add_tag_to_reading_tip(2,2))
    
    def test_check_if_tag_added_to_tip_works(self):
        self.tip_tags_repository.add_tag_to_reading_tip(1,1)
        self.assertTrue(self.tip_tags_repository.check_if_tag_added_to_tip(1,1))
        self.assertFalse(self.tip_tags_repository.check_if_tag_added_to_tip(1,10000))

    def test_get_all_tip_tag_pairs_works(self):
        tip_tag_pairs = self.tip_tags_repository.get_all_tip_tag_pairs()
        self.assertEqual(tip_tag_pairs, [(1,1)])
    
    def test_get_all_reading_tips_with_tag_id(self):
        tip_tag_pairs = self.tip_tags_repository.get_all_reading_tips_with_tag_id(1)
        self.assertEqual(tip_tag_pairs[0][1], 'Kirja 1')
        
        self.reading_tip_repository.create(ReadingTip(title="Kirja 2", author="Author 2", url="Link 2"))
        self.assertTrue(self.tip_tags_repository.add_tag_to_reading_tip(2,1))
