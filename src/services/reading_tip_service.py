from repositories.reading_tip_repository import (
    ReadingTipRepository as default_reading_tip_repository
    )
from entities.reading_tip import ReadingTip

class ReadingTipService:
    def __init__(self, reading_tip_repository=default_reading_tip_repository):
        self._reading_tip_repository = reading_tip_repository

    def create_reading_tip(self):
        title = input("Enter title: ")

        self._reading_tip_repository.create(ReadingTip(title=title, 
            author="another author", url="link for tip"))
        print("Testataan create_reading_tip")

    def delete_reading_tip_by_id(self, tip_id):
        """Delete selected reading tip by id
        """
        print("Testataan remove_reading_tip")

        self._reading_tip_repository.delete(tip_id)


    def search_reading_tip_by_title(self, tip_title):
        tips_with_title = self._reading_tip_repository.get_by_title(tip_title)

        if len(tips_with_title) == 0:
            print(f"Reading tips with title {tip_title} were not found.")
        else:
            print(f"Found {len(tips_with_title)} tips with title {tip_title}:")

            for title in tips_with_title:
                print(f"Title: {title[1]}")
                print(f"Author: {title[2]}")
                print(f"Url: {title[5]}\n")

    def modify_reading_tip(self):
        print("Testataan modify_reading_tip")
