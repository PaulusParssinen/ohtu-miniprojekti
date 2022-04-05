import unittest
from entities.reading_tip import ReadingTip

class TestReadingTip(unittest.TestCase):
    def setUp(self):
        self.reading_tip = ReadingTip(title='Tirakirja', reading_type='kirja', author='laaksonen')

    def test_string(self):
        self.assertEqual(str(self.reading_tip), 'Title: Tirakirja, Type: kirja, Author: laaksonen')
