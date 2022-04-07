import unittest

from database import Database

from entities.tag import Tag
from repositories.tags_repository import TagsRepository

class TestTagsRepository(unittest.TestCase):
    def setUp(self):
        self.db = Database(":memory:")
        self.tag = Tag('tag1')
        self.repository = TagsRepository(self.db)
        self.repository.create_tag(self.tag)

    def test_create_tag_with_non_empty_values_works(self):
        self.assertEqual(self.repository.get_tag_by_name('tag1').tag_name, "tag1")

    def test_create_tag_with_empty_field_should_return_false(self):
        self.assertFalse(self.repository.create_tag(Tag(" ")))