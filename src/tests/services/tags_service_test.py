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

    def test_create_with_valid_name_should_add_a_new_tag(self):
        self.service.create_tag("tag")
        added_tag = self.service.get_tag_by_name("tag")
        self.assertEqual("tag", added_tag.tag_name)

    def test_cannot_add_same_tags_multiple_times(self):
        self.service.create_tag('tag')
        self.assertFalse(self.service.create_tag('tag'))

    def test_get_all_tags_returns_correct_values(self):
        self.service.create_tag("tag1")
        self.service.create_tag("tag2")
        all_tags = self.service.get_all_tags()
        self.assertEqual(len(all_tags), 2)
        self.assertEqual(all_tags[0].tag_name, "tag1")
        self.assertEqual(all_tags[1].tag_name, "tag2")

    def test_get_tag_id_returns_correct_value(self):
        self.service.create_tag('tag1')
        tag = self.service.get_tag_id('tag1')
        self.assertEqual(tag, 1)

    def test_empty_title_should_return_false(self):
        self.assertFalse(self.service.create_tag(""))
