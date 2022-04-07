from repositories.tags_repository import (
    TagsRepository as default_tags_repository
    )

from entities.tag import Tag

class TagsService:
    def __init__(self, tags_repository=default_tags_repository):
        self._tags_repository = tags_repository

    def create_tag(self, tag_name):
        """Creates a new tag to the underlying Tags repository.

           Raises an exception if given fields do not follow the validation rules.
        """
        if not self._tags_repository.create_tag(tag_name):
            raise Exception("Failed to add a new tag!")

    def get_tag_by_name(self, tag_name):
        return self._tags_repository.get_tag_by_name(tag_name)

    def get_all_tags(self):
        """Returns all reading tips from the underlying repository.
        """
        return self._tags_repository.get_all_tags()
