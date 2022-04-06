class ReadingTip:

    """Class that represents the reading tip."""

    def __init__(self, identifier=None, title=None, reading_type=None,
                author=None, isbn=None, url=None, description=None, comment=None, tags=None, tag_id=None):
        self.id = identifier
        self.title = title
        self.author = author
        self.type = reading_type
        self.isbn = isbn
        self.url = url
        self.description = description
        self.comment = comment
        self.related_courses = []
        self.tags = tags
        self.tag_id = tag_id

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
        if self.tags:
            values.append(f"Tags:' {self.tags}")

        return seperator.join(values)

    def __str__(self):
        return self.format()
