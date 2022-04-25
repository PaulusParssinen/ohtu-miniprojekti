class Tag:
    """Class that represents a tag."""
    def __init__(self, tag_id, tag_name: str):
        self.tag_id = tag_id
        self.tag_name = tag_name

    def __str__(self):
        return self.tag_name

    def __repr__(self):
        return self.tag_name