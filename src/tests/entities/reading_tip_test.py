import unittest
from entities.reading_tip import ReadingTip

class TestGameBoard(unittest.TestCase):
    def setUp(self):
        self.reading_tip = ReadingTip('Tirakirja', 'kirja', 'laaksonen')

    def test_string(self):
        self.assertEqual(self.reading_tip.string(), 
                        'Otsikko: Tirakirja \n Tyyppi: kirja \n Author: laaksonen')
