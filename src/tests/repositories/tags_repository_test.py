import unittest

from database import Database

from entities.reading_tip import ReadingTip
from repositories.tags_repository import TagsRepository

class TestTagsRepository(unittest.TestCase):
    def setUp(self):
        self.db = Database(":memory:")
        self.repository = TagsRepository(self.db)

    def test_create_tag(self):
        pass