import unittest
from ui.console_table import ConsoleTable
from entities.reading_tip import ReadingTip
from rich.table import Table, Column

class TestConsoleTable(unittest.TestCase):
    def setUp(self):
        self.console_table = ConsoleTable()
        self.console_table._table = Table(show_header=True)
    
    def test_add_correct_number_of_rows(self):
        tip = ReadingTip(title="Title 1", author="Author 1")
        tip2 = ReadingTip(title="Title 2", author="Author 2")

        tips = [tip, tip2]
        
        self.console_table.add_rows(tips, [[],[]])

        rows = self.console_table._table.row_count

        self.assertEqual(rows, 2)

    def test_tag_lists_to_string_works(self):
        tags = []
        self.assertEqual(self.console_table.tag_lists_to_string(tags), "")

        tags = ["tag", "tag 2"]
        self.assertEqual(self.console_table.tag_lists_to_string(tags), "tag tag 2 ")