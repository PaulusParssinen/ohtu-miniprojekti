from repositories.reading_tip_repository import (
    ReadingTipRepository as default_reading_tip_repository
    )
from entities.reading_tip import ReadingTip

class ReadingTipService:
    """Class encapsulating the business logic exposed to the application.
    """
    def __init__(self, reading_tip_repository=default_reading_tip_repository):
        self._reading_tip_repository = reading_tip_repository

    def create_reading_tip(self, title, author=None, link=None):
        """Adds a new tip with given fields to the underlying repository.
           
           Raises an exception if given fields do not follow the validation rules.
        """
        title = title.rstrip()
        if len(title) == 0:
            raise Exception("Reading tip must have a title!")
        
        reading_tip = ReadingTip(title=title, author=author, url=link)
        
        if not self._reading_tip_repository.create(reading_tip):
            raise Exception("Failed to add a new reading tip!")

    def delete_reading_tip_by_id(self, tip_id):
        """Delete selected reading tip by id
        """
        if not self._reading_tip_repository.delete(tip_id):
            raise Exception(f"Failed to delete reading tip with given id: {tip_id}")

    def see_all_reading_tips(self) -> list[ReadingTip]:
        """Returns all reading tips from the underlying repository.
        """
        return self._reading_tip_repository.get_all()
    
    def search_reading_tip_by_title(self, tip_title) -> list[ReadingTip]:
        """Returns reading tips by found from the underlying repository by given title.
        
           If no tips were found from the repository, returns None.
        """
        tips_with_title = self._reading_tip_repository.search_by_title(tip_title)
        return tips_with_title

    def get_reading_tip_by_id(self, tip_id) -> ReadingTip:
        """Returns reading tip by given id from the underlying repository.
        
           If reading tip on given id does not exist in the repository, returns None.
        """
        return self._reading_tip_repository.get_by_id(tip_id)

    def modify_reading_tip_by_id(self, reading_tip_id: int,
            new_title=None, new_author=None, new_url=None) -> bool:
        """Modifies given reading tip fields in the underlying repository.
        
           If given reading tip was modified succesfully, returns True.
           If given reading tip id does not exist in the repository, returns False
        """
        tip = self.get_reading_tip_by_id(reading_tip_id)
        if tip is None:
            return False
        
        return self.modify_reading_tip(tip, new_title, new_author, new_url)

    def modify_reading_tip(self, reading_tip: ReadingTip,
            new_title=None, new_author=None, new_url=None) -> bool:
        """Modifies given reading tip fields in the underlying repository.
        
           If given reading tip was modified succesfully, returns True.
           If given reading tip id does not exist in the repository, returns False
        """
        # Update fields in the existing ReadintTip object if new values are specified
        if new_title:
            reading_tip.title = new_title
        if new_author:
            reading_tip.author = new_author
        if new_url:
            reading_tip.url = new_url
        
        return self._reading_tip_repository.modify(reading_tip)
