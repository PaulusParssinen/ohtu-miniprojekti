from console_io import ConsoleIO
from services.reading_tip_service import ReadingTipService
from app import App

def main():
    
    #reading_tip_repository = ReadingTipRepository()
    reading_tip_service = ReadingTipService()
    console_io = ConsoleIO()
    app = App(reading_tip_service, console_io)

    app.run()

if __name__ == "__main__":
    main()
