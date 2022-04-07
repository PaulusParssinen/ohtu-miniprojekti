class Tags:
    def __init__(self):
        self.tags = []
        self.tags_in_reading_tip = []

    def create_new_tag(self, tag_name):
        """Creates new tag to the """
        if tag_name not in self.tags:
            self.tags.append(tag_name)

    def add_tag_to_reading_tip(self, tag_name):
        if tag_name not in self.tags:
            self.tags_in_reading_tip.append(tag_name)
