from rich.console import Console
from rich.table import Table
from entities.reading_tip import ReadingTip

class ConsoleTable:
    def __init__(self):
        self._console = Console()
        self._table = 0
    
    def create_table(self, reading_tips):
        self._table = Table(show_header=True)
        self.set_columns()
        self.add_rows(reading_tips)
        self.print()
    
    def set_columns(self):
        self._table.add_column("Id")
        self._table.add_column("Title")
        self._table.add_column("Url")

    def add_rows(self, reading_tips):
        for tip in reading_tips:
            self._table.add_row(str(tip.id), str(tip.title), str(tip.url))
    
    def print(self):
        self._console.print(self._table)
