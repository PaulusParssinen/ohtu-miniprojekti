import unittest
from entities.tag import Tag

class TestReadingTip(unittest.TestCase):
    def setUp(self):
        self.tag = Tag("tag1")

    def test_return_value(self):
        self.assertEqual(self.tag.tag_name, "tag1")
        self.assertEqual(self.tag.__repr__(), "tag1")
