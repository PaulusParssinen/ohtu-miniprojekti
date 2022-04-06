from app import App
from database import Database
from tests.stub_io import StubIO
from services.reading_tip_service import ReadingTipService
from repositories.reading_tip_repository import ReadingTipRepository

class AppLibrary:
    def __init__(self):
        self._io = StubIO()
        self._db = Database(":memory:")
        self._repository = ReadingTipRepository(self._db)
        self._service = ReadingTipService(self._repository)

        self._app = App(self._service, self._io)

    def input(self, value):
        self._io.add_input(value)

    def output_should_contain(self, value):
        outputs = self._io.outputs

        if not value in outputs:
            raise AssertionError(f"Output \"{value}\" is not in {str(outputs)}")

    def run_application(self):
        self._app.run()

    def create_reading_tip(self, title, link):
        self._service.create(title, link=link)
