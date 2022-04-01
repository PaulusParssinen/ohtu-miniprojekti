
from services.reading_tip_service import ReadingTipService
from repositories.reading_tip_repository import ReadingTipRepository
from ui.console_io import ConsoleIO
from ui.app import App

def main():

    #reading_tip_repository = ReadingTipRepository()
    database = ReadingTipRepository()
    reading_tip_service = ReadingTipService(database)
    console_io = ConsoleIO()
    app = App(reading_tip_service, console_io)

    app.run()

if __name__ == "__main__":
    main()
