import unittest

from database import Database

from entities.tag import Tag

from services.tags_service import TagsService
from services.tip_tags_service import TipTagsService
from services.reading_tip_service import ReadingTipService

from repositories.tags_repository import TagsRepository
from repositories.tip_tags_repository import TipTagsRepository
from repositories.reading_tip_repository import ReadingTipRepository

class TestReadingTipTagsService(unittest.TestCase):
    def setUp(self):
        self.db = Database(":memory:")
        
        self.tags_repository = TagsRepository(self.db)
        self.tip_tags_repository = TipTagsRepository(self.db)
        self.reading_tip_repository = ReadingTipRepository(self.db)
        
        self.tags_service = TagsService(self.tags_repository)
        self.reading_tip_service = ReadingTipService(self.reading_tip_repository)
        self.tip_tags_service = TipTagsService(self.tip_tags_repository, 
            self.tags_service, self.reading_tip_service)
        
        self.tags_service.create_tag("Käpistely")
        self.reading_tip_service.create(title="Tirakirja")
        self.tip_tags_service.add_tag_to_reading_tip(1, 1)

    def test_add_tag_to_reading_tip_works(self):
        self.assertTrue(self.tip_tags_service.add_tag_to_reading_tip(2,2))

    def test_check_if_tag_added_to_tip_works(self):
        self.assertTrue(self.tip_tags_service.check_if_tag_added_to_tip(1,1))

    def test_get_all_tip_tag_pairs_works(self):
        tip_tag_pairs = self.tip_tags_service.get_all_tip_tag_pairs()
        self.assertEqual(tip_tag_pairs, [(1,1)])

    def test_get_all_reading_tips_with_tag_id_works(self):
        reading_tip_objects = self.tip_tags_service.get_all_reading_tips_with_tag_id(1)
        self.assertEqual(reading_tip_objects[0].title, 'Tirakirja')

    def test_get_all_tags_with_tip_id_works(self):
        tags = self.tip_tags_service.get_all_tags_with_tip_id(1)
        self.assertListEqual(tags, [Tag(1, "Käpistely")])

        self.tags_service.create_tag("Algot")
        self.tip_tags_service.add_tag_to_reading_tip(1, 2)

        names = self.tip_tags_service.get_all_tags_with_tip_id(1)
        self.assertListEqual(names, [Tag(1, "Käpistely"), Tag(2, "Algot")])

    def test_get_all_tags_for_multiple_ids_works(self):
        cses_book_id = self.reading_tip_service.create(title = "Competitive Programmer’s Handbook")

        self.tags_service.create_tag("Algot")
        self.tip_tags_service.add_tag_to_reading_tip(cses_book_id, 2)

        names = self.tip_tags_service.get_all_tags_for_multiple_ids([1, cses_book_id])
        self.assertListEqual(names, [[Tag(1, "Käpistely")], [Tag(2, "Algot")]])
