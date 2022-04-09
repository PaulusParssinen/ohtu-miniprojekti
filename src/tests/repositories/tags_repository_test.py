import unittest

from database import Database

from entities.tag import Tag
from repositories.tags_repository import TagsRepository

class TestTagsRepository(unittest.TestCase):
    def setUp(self):
        self.db = Database(":memory:")
        self.repository = TagsRepository(self.db)

    def test_create_tag_with_non_empty_values_works(self):
        self.repository.create_tag('tag')
        added_tag = self.repository.get_tag_by_name("tag")
        self.assertEqual("tag", added_tag.tag_name)

    def test_cannot_add_same_tags_multiple_times(self):
        self.assertTrue(self.repository.create_tag('tag'))
        self.repository.create_tag('tag')
        self.assertFalse(self.repository.create_tag('tag'))

    def test_get_all_tags_returns_correct_values(self):
        self.repository.create_tag("tag1")
        self.repository.create_tag("tag2")
        all_tags = self.repository.get_all_tags()
        self.assertEqual(len(all_tags), 2)
        self.assertEqual(all_tags[0].tag_name, "tag1")
        self.assertEqual(all_tags[1].tag_name, "tag2")

    def test_get_tag_id_returns_correct_value(self):
        self.repository.create_tag('tag1')
        tag = self.repository.get_tag_id('tag1')
        self.assertEqual(tag, 1)

    def test_empty_tag_id_should_raise_error(self):
        self.assertEqual(self.repository.get_tag_id(""), None)