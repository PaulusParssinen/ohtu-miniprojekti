from ui.app import App
from ui.console_table import ConsoleTable
from database import Database
from tests.stub_io import StubIO
from services.reading_tip_service import ReadingTipService
from services.tags_service import TagsService
from services.tip_tags_service import TipTagsService
from repositories.reading_tip_repository import ReadingTipRepository
from repositories.tags_repository import TagsRepository
from repositories.tip_tags_repository import TipTagsRepository

class AppLibrary:
    def __init__(self):
        self._io = StubIO()
        self._db = Database(":memory:")
        
        self._tags_repository = TagsRepository(self._db)
        self._tip_tags_repository = TipTagsRepository(self._db)
        self._reading_tip_repository = ReadingTipRepository(self._db)
        
        self._tag_service = TagsService(self._tags_repository)
        self._reading_tip_service = ReadingTipService(self._reading_tip_repository)
        self._tip_tags_service = TipTagsService(self._tip_tags_repository, self._tag_service, 
            self._reading_tip_service)
        
        self._table = ConsoleTable()
        self._app = App(self._reading_tip_service, self._io, self._tag_service,
                        self._tip_tags_service, self._table)

    def input(self, value):
        self._io.add_input(value)

    def output_should_contain(self, value):
        outputs = self._io.outputs

        if not value in outputs:
            raise AssertionError(f"Output \"{value}\" is not in {str(outputs)}")

    def run_application(self):
        self._app.run()

    def create_reading_tip(self, title, link):
        self._reading_tip_service.create(title, link=link, status="Not read yet!")

    def table_row_count_should_be(self, value):
        row_count = self._table.get_row_count()

        if int(row_count) != int(value):
            raise AssertionError(f"Row count {row_count} is not {value}")
