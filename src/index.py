import sys

from database import db

from services.reading_tip_service import ReadingTipService
from repositories.reading_tip_repository import ReadingTipRepository

from ui.app import App
from ui.console_io import ConsoleIO

def main():
    reading_tip_repository = ReadingTipRepository(db)
    reading_tip_service = ReadingTipService(reading_tip_repository)
    
    console_io = ConsoleIO()
    
    app = App(reading_tip_service, console_io)
    app.run()

if __name__ == "__main__":
    # Allow database to dropped
    if len(sys.argv) > 1 and sys.argv[1].lower() == "--reset-database":
        db.reset_database()
    
    main()
