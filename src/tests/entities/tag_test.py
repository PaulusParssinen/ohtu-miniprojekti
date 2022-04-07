import unittest
from entities.tag import Tag

class TestReadingTip(unittest.TestCase):
    def test_return_value(self):
        self.assertEqual(Tag("tag1").tag_name, "tag1")
