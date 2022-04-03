from repositories.reading_tip_repository import (
    ReadingTipRepository as default_reading_tip_repository
    )

class ReadingTipService:
    def __init__(self, reading_tip_repository=default_reading_tip_repository):
        self._reading_tip_repository = reading_tip_repository

    def create_reading_tip(self):
        #self._reading_tip_repository.create(ReadingTip())
        print("Testataan create_reading_tip")

    def delete_reading_tip_by_id(self, tip_id):
        """Delete selected reading tip by id
        """
        print("Testataan remove_reading_tip")

        self._reading_tip_repository.delete(tip_id)


    def search_reading_tip_by_title(self, title):
        titles = self._reading_tip_repository.get_by_title(title)

        if len(titles) == 0:
            print(f"Reading tips with title {title} were not found.")
        else:
            for title in titles:
                print("Käsitellään tuplet ja tulostetaan ne.")

    def modify_reading_tip(self):
        print("Testataan modify_reading_tip")
