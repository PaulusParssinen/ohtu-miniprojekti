import unittest
from entities.reading_tip import ReadingTip

class TestReadingTip(unittest.TestCase):

    def test_str_format_correct_only_title_and_author_defined(self):
        reading_tip = ReadingTip(title='Tirakirja', author='laaksonen', url='wwww.tira.fi', status="Not read yet!")
        self.assertEqual(str(reading_tip), 'Title: Tirakirja, Author: laaksonen, URL: wwww.tira.fi, Status: Not read yet!')

    def test_str_format_correct_when_all_fields_are_defined(self):
        reading_tip = ReadingTip(identifier=42, title='Tirakirja', reading_type='kirja', author='laaksonen', status="Not read yet!")
        self.assertEqual(str(reading_tip), 'Id: 42, Title: Tirakirja, Type: kirja, Author: laaksonen, Status: Not read yet!')

    def test_str_format_shows_status_none_when_no_field_is_defined(self):
        reading_tip = ReadingTip()
        self.assertEqual(str(reading_tip), "Status: None")
