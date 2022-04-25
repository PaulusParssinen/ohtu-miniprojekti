import unittest
from entities.tag import Tag

class TestTag(unittest.TestCase):
    def setUp(self):
        self.tag = Tag(1, "tag1")

    def test_return_value(self):
        self.assertEqual(self.tag.tag_id, 1)
        self.assertEqual(self.tag.tag_name, "tag1")
        self.assertEqual(self.tag.__repr__(), "tag1")
