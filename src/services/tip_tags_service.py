from repositories.tip_tags_repository import (
    TipTagsRepository as default_tip_tags_repository
    )

from entities.reading_tip import ReadingTip
from entities.tag import Tag

class TipTagsService:
    def __init__(self, tip_tags_repository=default_tip_tags_repository):
        self._tip_tags_repository = tip_tags_repository

    def add_tag_to_reading_tip(self, tip_id, tag_id):
        return self._tip_tags_repository.add_tag_to_reading_tip(tip_id, tag_id)

    def check_if_tag_added_to_tip(self, tip_id, tag_id):
        return self._tip_tags_repository.check_if_tag_added_to_tip(tip_id, tag_id)
    
    def get_all_tip_tag_pairs(self):
        return self._tip_tags_repository.get_all_tip_tag_pairs()
