class ReadingTip:

    """Class that represents the reading tip."""

    def __init__(self, identifier=None, title=None, reading_type=None,
                author=None, isbn=None, url=None, description=None, comment=None):
        self.id = identifier
        self.title = title
        self.author = author
        self.type = reading_type
        self.isbn = isbn
        self.url = url
        self.description = description
        self.comment = comment
        self.related_courses = []
        self.tags = []
        self.tags_in_reading_tip = []

    def create_new_tag(self, tag_name):
        """Creates new tag to the """
        if tag_name not in self.tags:
            self.tags.append(tag_name)

    def add_tag_to_reading_tip(self, tag_name):
        if tag_name not in self.tags:
            self.tags_in_reading_tip.append(tag_name)

    def format(self, seperator=", ") -> str:
        """Formats the reading tip values to a string using the specified seperator (default ", ").
        """
        values = []
        if self.id:
            values.append(f"Id: {self.id}")
        if self.title:
            values.append(f"Title: {self.title}")
        if self.type:
            values.append(f"Type: {self.type}")
        if self.author:
            values.append(f"Author: {self.author}")
        if self.url:
            values.append(f"URL: {self.url}")
        if self.tags_in_reading_tip:
            values.append(f"Tags: {self.tags}")
        return seperator.join(values)

    def __str__(self):
        return self.format()
