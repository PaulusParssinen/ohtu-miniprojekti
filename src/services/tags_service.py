from repositories.tags_repository import (
    TagsRepository as default_tags_repository
    )

class TagsService:
    def __init__(self, tags_repository=default_tags_repository):
        self._tags_repository = tags_repository

    def get_tag_by_id(self, tag_id):
        return self._tags_repository.get_tag_by_id(tag_id)

    def get_all_tags(self):
        pass
