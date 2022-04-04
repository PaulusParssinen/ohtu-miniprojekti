from db_connection import get_db_connection

from services.reading_tip_service import ReadingTipService
from repositories.reading_tip_repository import ReadingTipRepository

from ui.app import App
from ui.console_io import ConsoleIO

def main():

    db_connection = get_db_connection()
    reading_tip_repository = ReadingTipRepository(db_connection)
    reading_tip_service = ReadingTipService(reading_tip_repository)
    
    console_io = ConsoleIO()
    
    app = App(reading_tip_service, console_io)
    app.run()

if __name__ == "__main__":
    main()
