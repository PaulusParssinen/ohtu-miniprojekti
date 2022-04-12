import unittest
from database import Database
from services.tip_tags_service import TipTagsService
from repositories.tip_tags_repository import TipTagsRepository
from services.reading_tip_service import ReadingTipService
from repositories.reading_tip_repository import ReadingTipRepository
from services.tags_service import TagsService
from repositories.tags_repository import TagsRepository

class TestReadingTipTagsService(unittest.TestCase):
    def setUp(self):
        self.db = Database(":memory:")
        self.tip_tags_repository = TipTagsRepository(self.db)
        self.reading_tip_repository = ReadingTipRepository(self.db)
        self.tip_tags_service = TipTagsService(self.tip_tags_repository)
        self.reading_tip_service = ReadingTipService(self.reading_tip_repository)
        self.tags_repository = TagsRepository(self.db)
        self.tags_service = TagsService(self.tags_repository)

        self.tip_tags_service.add_tag_to_reading_tip(1,1)
        self.reading_tip_service.create(title="Kirja 1")

    def test_add_tag_to_reading_tip_works(self):
        self.assertTrue(self.tip_tags_service.add_tag_to_reading_tip(2,2))

    def test_check_if_tag_added_to_tip_works(self):
        self.assertTrue(self.tip_tags_service.check_if_tag_added_to_tip(1,1))

    def test_get_all_tip_tag_pairs_works(self):
        tip_tag_pairs = self.tip_tags_service.get_all_tip_tag_pairs()
        self.assertEqual(tip_tag_pairs, [(1,1)])

    def test_get_all_reading_tips_with_tag_id_works(self):
        reading_tip_objects = self.tip_tags_service.get_all_reading_tips_with_tag_id(1)
        self.assertEqual(reading_tip_objects[0].title, 'Kirja 1')

    def test_get_all_tags_with_tip_id_works(self):
        id = self.reading_tip_service.create(title = "Book 2")

        tags = self.tip_tags_service.get_all_tags_with_tip_id(id)
        self.assertEqual(tags, [])

        self.tags_service.create_tag("tag")
        self.tags_service.create_tag("another")

        self.tip_tags_service.add_tag_to_reading_tip(id, 1)
        self.tip_tags_service.add_tag_to_reading_tip(id, 2)

        tags = self.tip_tags_service.get_all_tags_with_tip_id(id)
        self.assertEqual(tags, ["tag", "another"])

    def test_get_all_tags_for_multiple_ids_works(self):
        id = self.reading_tip_service.create(title = "Book 2")
        id2 = self.reading_tip_service.create(title = "Book 2")

        self.tags_service.create_tag("tag")
        self.tags_service.create_tag("another")

        self.tip_tags_service.add_tag_to_reading_tip(id, 1)
        self.tip_tags_service.add_tag_to_reading_tip(id2, 2)

        tags = self.tip_tags_service.get_all_tags_for_multiple_ids([id, id2])
        self.assertEqual(tags, [["tag"], ["another"]])
