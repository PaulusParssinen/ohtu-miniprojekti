import unittest

from database import Database

from entities.tag import Tag
from repositories.tags_repository import TagsRepository

class TestTagsRepository(unittest.TestCase):
    def setUp(self):
        self.db = Database(":memory:")
        self.repository = TagsRepository(self.db)

    def test_get_all_tags(self):
        pass
        