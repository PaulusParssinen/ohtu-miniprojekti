import unittest
from unittest.mock import Mock, ANY
from entities.reading_tip import ReadingTip
from ui.app import App
from database import db
from services.reading_tip_service import ReadingTipService
from services.tags_service import TagsService
from services.tip_tags_service import TipTagsService
from repositories.reading_tip_repository import ReadingTipRepository
from repositories.tags_repository import TagsRepository
from repositories.tip_tags_repository import TipTagsRepository
from ui.console_io import ConsoleIO
from ui.console_table import ConsoleTable
from ui.app import App

class TestApp(unittest.TestCase):
    def setUp(self):
        self.reading_tip_service_mock = Mock(wraps=ReadingTipService(ReadingTipRepository(db)))
        self.tag_service_mock = Mock(wraps=TagsService(TagsRepository(db)))
        self.tip_tags_service_mock = Mock(wraps=TipTagsService(TipTagsRepository(db)))
        self.mock_io = Mock(wraps=ConsoleIO())
        self.table_mock = Mock(wraps=ConsoleTable())

        self.app = App(self.reading_tip_service_mock, self.mock_io,
                            self.tag_service_mock, self.tip_tags_service_mock,
                            self.table_mock)
        self.tip_mock = Mock(wraps=ReadingTip)
        self.tip_mock.title = "Muumit"
        self.tip_mock.id = "2"

    def test_command_with_unvalid_value_is_not_called(self):
        self.app.get_command("100")
        self.reading_tip_service_mock.assert_not_called()

    def test_command_get_all_is_called(self):
        self.app.get_command("4")
        self.reading_tip_service_mock.get_all.assert_called()

    def test_command_see_all_tags_is_called(self):
        self.app.get_command("9")
        self.tag_service_mock.get_all_tags.assert_called()

    def test_find_tip_by_name_is_called(self):
        self.mock_io.write.side_effect = ["1"]

    def test_creating_and_deleting_reading_tip_is_called(self):
        inputs = ["1", "Muumien tarinoita", "www.muumit.fi", "Tove Jansson", "kuvailu", "kommentit", "muumi_tag", "11"]
        self.mock_io.read.side_effect = inputs
        self.app.run()
        self.reading_tip_service_mock.create.assert_called()

    def test_modyfing_reading_tip_is_called(self):
        inputs = ["2", "1", "Muumilaakson tarinoita", "11"]
        self.mock_io.read.side_effect = inputs
        self.app.run()
        self.reading_tip_service_mock.update.assert_called()

    def test_deleting_tip_is_called(self):
        inputs = ["3", "2", "11"]
        self.mock_io.read.side_effect = inputs
        self.app.run()
        self.reading_tip_service_mock.delete.assert_called()

    def test_see_reading_tips_by_title_is_called(self):
        inputs = ["5", "Muumilaakson tarinoita","11"]
        self.mock_io.read.side_effect = inputs
        self.app.run()
        self.reading_tip_service_mock.search_by_title.assert_called()
