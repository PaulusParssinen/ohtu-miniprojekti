import sys
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
import colorama
from colorama import Fore, Back, Style

def main():
    reading_tip_repository = ReadingTipRepository(db)
    reading_tip_service = ReadingTipService(reading_tip_repository)

    reading_tip_service.create(title="Kirja", link=None, author="Kirjoittaja", description=None, comment=None, status="Not read yet!")
    reading_tip_service.create(title="Luettu kirja", link=None, author="Kirjoittaja", description=None, comment=None, status="Already read!")
    reading_tip_service.create(title="Kirja 2", link=None, author="Kirjoittaja", description="Tämä on kuvaus", comment=None, status="Not read yet!")
    reading_tip_service.create(title="Vinkki", link=None, author="Kirjoittaja", description=None, comment="Tämä on kommentti", status="Already read!")
    reading_tip_service.create(title="HS", link="www.hs.fi", author="Kirjoittaja", description=None, comment="Tämä on kommentti", status="Already read!")

    kissa = "kissa"
    testi = Fore.GREEN+kissa+Style.RESET_ALL
    print(testi)
    print(type(testi))


def write_green(self, value, end='\n'):
        print(Fore.GREEN+value+Style.RESET_ALL, end=end)

def write_red(self, value, end='\n'):
        print(Fore.RED+value+Style.RESET_ALL, end=end)

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1].lower() == "--reset-database":
        db.reset_database()

    main()