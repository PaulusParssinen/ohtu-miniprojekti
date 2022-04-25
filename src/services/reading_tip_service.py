import requests

from repositories.reading_tip_repository import ReadingTipRepository as default_tip_repository
from entities.reading_tip import ReadingTip

class ReadingTipService:
    """Class encapsulating the business logic such as exposed to the application.

       This class is responsible for validating and sanitizing parameters to be valid the
       for underlying data storage.
    """
    def __init__(self, reading_tip_repository=default_tip_repository):
        self._reading_tip_repository = reading_tip_repository
    
    def create(self, title: str, author=None, link=None,
                description=None, comment=None, status=None) -> int:
        """Adds a new tip with given fields to the underlying repository.
           
           If tip was added successfully, returns the inserted row (tip id).
           If the operation fails, for example the given tip link was invalid, returns None.
        """
        
        reading_tip = ReadingTip(title=title, author=author, url=link,
            description=description, comment=comment, status=status)

        # Validate and process tip fields before insert.
        if not self.validate_tip(reading_tip):
            return None

        return self._reading_tip_repository.create(reading_tip)

    def delete(self, tip_id):
        """Delete selected reading tip by id
        """
        self._reading_tip_repository.delete(tip_id)


    def get_all(self):
        """Returns all reading tips from the underlying repository.
        """

        return self._reading_tip_repository.get_all()
    
    def get_unread(self):
        """Returns all unread reading tips from the underlying repository.
        """

        return self._reading_tip_repository.get_unread()

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

    def update(self, new_reading_tip: ReadingTip) -> bool:
        """Updates given reading tip fields in the underlying repository.
        """
        
        # Fetch the existing tip from the underlying repository
        existing_tip = self.get_by_id(new_reading_tip.id)
        if new_reading_tip is None or existing_tip is None:
            return False
        
        # Validate the new values.
        if not self.validate_tip(new_reading_tip):
            return False

        return self._reading_tip_repository.update(new_reading_tip)

    def update_status(self, reading_tip_status):
        if reading_tip_status is None:
            return False
        return self._reading_tip_repository.update_status(reading_tip_status)

    def validate_tip(self, reading_tip: ReadingTip) -> bool:
        """Validate the entire reading tip object before inserting or 
           updating it to the underlying repository.
           
           If the reading tip was valid, returns True.
        """ 
        if self.validate_title(reading_tip.title):
            return False
        
        # If link was given, attempt to shorten it.
        if reading_tip.url:
            reading_tip.url = self.shorten_tip_url(reading_tip.url)
            # if shortened link is now None, the URL given by user was malformed => fail.
            if not reading_tip.url:
                return False
        
        return True
        
    def validate_title(self, title) -> str:
        """Validates the tip title.
           
           If the title was valid, returns None.
           If the title was invalid, returns the reason.
        """
        title = title.strip()
        if len(title) == 0:
            return 'Empty title'

        if len(title) > 200:
            return 'Too many characters'

        return None
    
    def shorten_tip_url(self, tip_url: str) -> str:
        """Attempts to convert the given tip URL to shortened one using TinyURL API.
           
           If conversion was successful, returns the shortened URL.
           If given URL was invalid or the request failed for some other reason; returns None.
        """
        try:
            return requests.get("https://tinyurl.com/api-create.php", params=dict(url=tip_url)).text
        except Exception:
            # TinyURL returns 4xx error code if the request was invalid.
            return None
    
    def get_ids(self, reading_tips):
        """Create a list of reading tip ids
        """

        ids = []
        for tip in reading_tips:
            ids.append(tip.id)
        return ids
