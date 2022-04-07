import unittest

from database import Database

from entities.tag import Tag
from services.tags_service import TagsService
from repositories.tags_repository import TagsRepository

class TestReadingTipService(unittest.TestCase):
    def setUp(self):
        self.db = Database(":memory:")
        self.repository = TagsRepository(self.db)
        self.service = TagsService(self.repository)
        self.service.create_tag(Tag("tagi1"))

    def test_create_with_valid_name_should_add_a_new_tag(self):
        self.assertEqual(self.service.get_by_tag_name("tagi1"), "tagi1")
