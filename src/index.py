import sys
from database import db
from services.reading_tip_service import ReadingTipService
from services.tags_service import TagsService
from repositories.reading_tip_repository import ReadingTipRepository
from repositories.tags_repository import TagsRepository
from ui.console_io import ConsoleIO
from ui.console_table import ConsoleTable
from app import App

def main():
    reading_tip_repository = ReadingTipRepository(db)
    tag_repository = TagsRepository(db)
    reading_tip_service = ReadingTipService(reading_tip_repository)
    tag_service = TagsService(tag_repository)
    console_io = ConsoleIO()
    console_table = ConsoleTable()

    app = App(reading_tip_service, console_io, tag_service, console_table)
    app.run()

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1].lower() == "--reset-database":
        db.reset_database()

    main()
