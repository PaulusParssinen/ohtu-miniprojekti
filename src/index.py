import sys

from database import db

from services.tags_service import TagsService
from services.tip_tags_service import TipTagsService
from services.reading_tip_service import ReadingTipService

from repositories.tags_repository import TagsRepository
from repositories.tip_tags_repository import TipTagsRepository
from repositories.reading_tip_repository import ReadingTipRepository

from ui.app import App
from ui.console_io import ConsoleIO
from ui.console_table import ConsoleTable

def main():
    tag_repository = TagsRepository(db)
    tip_tags_repository = TipTagsRepository(db)
    reading_tip_repository = ReadingTipRepository(db)
    
    tag_service = TagsService(tag_repository)
    reading_tip_service = ReadingTipService(reading_tip_repository)
    tip_tags_service = TipTagsService(tip_tags_repository, tag_service, reading_tip_service)
    
    console_io = ConsoleIO()
    console_table = ConsoleTable()

    app = App(reading_tip_service, console_io, tag_service, tip_tags_service, console_table)
    app.run()

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1].lower() == "--reset-database":
        db.reset_database()

    main()
