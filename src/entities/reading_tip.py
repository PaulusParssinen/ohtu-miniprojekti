class ReadingTip:

    """Class that represents the reading tip."""

    def __init__(self, title=None, reading_type=None, 
                author=None, isbn=None, url=None, description=None):
        self.title = title
        self.author = author
        self.type = reading_type
        self.isbn = isbn
        self.url = url
        self.description = description
        self.comment = ''
        self.related_courses = []

    def string(self):
        return f"Otsikko: {self.title} \n Tyyppi: {self.type} \n Author: {self.author}"

    def __str__(self):
        pass
