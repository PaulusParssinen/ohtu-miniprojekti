from repositories.reading_tip_repository import (
    ReadingTipRepository as default_reading_tip_repository
    )
from entities.reading_tip import ReadingTip

class ReadingTipService:
    """Class encapsulating the business logic such as exposed to the application.

       This class is responsible for validating and sanitizing parameters to be valid the 
       for underlying data storage.
    """
    def __init__(self, reading_tip_repository=default_reading_tip_repository):
        self._reading_tip_repository = reading_tip_repository

    def create(self, title: str, author=None, link=None):
        """Adds a new tip with given fields to the underlying repository.

           Raises an exception if given fields do not follow the validation rules.
        """
        self.validate_title(title)

        reading_tip = ReadingTip(title=title, author=author, url=link)

        if not self._reading_tip_repository.create(reading_tip):
            raise Exception("Failed to add a new reading tip!")

    def delete(self, tip_id):
        """Delete selected reading tip by id
        """
        self._reading_tip_repository.delete(tip_id)


    def get_all(self):
        """Returns all reading tips from the underlying repository.
        """
        return self._reading_tip_repository.get_all()

    def search_by_title(self, tip_title):
        """Returns reading tips by found from the underlying repository by given title.

           If no tips were found from the repository, returns None.
        """
        return self._reading_tip_repository.search_by_title(tip_title)

    def get_by_id(self, tip_id) -> ReadingTip:
        """Returns reading tip by given id from the underlying repository.

           If reading tip on given id does not exist in the repository, returns None.
        """
        return self._reading_tip_repository.get_by_id(tip_id)

    def update_by_id(self, reading_tip_id: int,
            new_title=None, new_author=None, new_url=None) -> bool:
        """Updates given reading tip fields in the underlying repository.

           If given reading tip was modified succesfully, returns True.
           If given reading tip id does not exist in the repository, returns False
        """
        tip = self.get_by_id(reading_tip_id)
        if tip is None:
            raise Exception(f"No reading tip found with id: {reading_tip_id}")

        # Edit the existing tip fields
        if new_title:
            tip.title = new_title
        if new_author:
            tip.author = new_author
        if new_url:
            tip.url = new_url

        return self.update(tip)

    def update(self, new_reading_tip: ReadingTip) -> bool:
        """Updates given reading tip fields in the underlying repository.
        """
        # Validate the fields of the new reading tip object
        self.validate_title(new_reading_tip.title)
        self._reading_tip_repository.update(new_reading_tip)

    def validate_title(self, title):
        # Remove whitespace from the start and end of the title
        title = title.strip()
        if len(title) == 0:
            raise Exception("Reading tip cannot have a empty title!")
