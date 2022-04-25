from repositories.tags_repository import (
    TagsRepository as default_tags_repository
    )

class TagsService:
    def __init__(self, tags_repository=default_tags_repository):
        self._tags_repository = tags_repository

    def create_tag(self, tag_name):
        """Creates a new tag to the underlying Tags repository
        """

        if self.check_if_tag_exists(tag_name):
            return False

        return self._tags_repository.create_tag(tag_name)

    def check_if_tag_exists(self, tag_name):
        """Check if tag is found in Tags repository
        """

        return self._tags_repository.check_if_tag_exists(tag_name)

    def get_tag_id(self, tag_name):
        """Returns tag that had been fetched from Tags Repository by tag name
        """

        return self._tags_repository.get_tag_id(tag_name)

    def get_tag_by_name(self, tag_name):
        """Fetches tag id from Tags repository by tag name
        """
        return self._tags_repository.get_tag_by_name(tag_name)

    def get_all_tags(self):
        """Returns all reading tips from the underlying Tags repository.
        """
        
        return self._tags_repository.get_all_tags()
