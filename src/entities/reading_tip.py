class ReadingTip:

    """Class that describes a reading tip."""

    def __init__(self, title, type, author, isbn=None, url=None, description=None, comment=None, related_courses=None):
        self.title = title
        self.author = author
        self.type = type
        self.isbn = isbn
        self.url = url
        self.description = description
        self.comment = comment
        self.related_courses = related_courses

    def string(self):
        return f"Otsikko: {self.title} \n Tyyppi: {self.type} \n Author: {self.author}"

    def __str__(self):
    # if self.type == 'book':
        #return self.string() + f" \n ISBN: {self.isbn}"
