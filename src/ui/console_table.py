from rich.console import Console
from rich.table import Table

class ConsoleTable:
    def __init__(self):
        self._console = Console()
        self._table = Table()

    def create_table(self, reading_tips, tags=None):
        self._table = Table(show_header=True, show_lines=True)
        self.set_columns()
        self.add_rows(reading_tips, tags)
        self.print()

    def set_columns(self):
        self._table.add_column("Id")
        self._table.add_column("Title")
        self._table.add_column("Author")
        self._table.add_column("Url")
        self._table.add_column("Description")
        self._table.add_column("Comments")
        self._table.add_column("Tags")
        self._table.add_column("Status")

    def add_rows(self, reading_tips, all_tags):
        tip_index = 0

        for tip in reading_tips:
            tags = self.tag_lists_to_string(all_tags[tip_index])

            if tip.status == "Already read!":
                emoji = ":white_heavy_check_mark:"
            else:
                emoji = ":cross_mark:"

            self._table.add_row(str(tip.id), str(tip.title), str(tip.author or ""), str(tip.url or ""),
                str(tip.description or ""), str(tip.comment or ""), str(tags or ""), emoji)
            tip_index += 1

    def tag_lists_to_string(self, tags):
        tag_string = ""

        for tag in tags:
            tag_string = tag_string + str(tag) + " "

        return tag_string

    def print(self):
        self._console.print(self._table)

    def get_row_count(self):
        return self._table.row_count
