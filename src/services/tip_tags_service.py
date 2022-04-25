from services.tags_service import TagsService as default_tags_service
from services.reading_tip_service import ReadingTipService as default_reading_tip_service

from repositories.tip_tags_repository import TipTagsRepository as default_tip_tags_repository

class TipTagsService:
    def __init__(self, 
                 tip_tags_repository=default_tip_tags_repository,
                 tags_service=default_tags_service, 
                 tips_service=default_reading_tip_service):
        self._tip_tags_repository = tip_tags_repository
        self._tags_service = tags_service
        self._tips_service = tips_service

    def add_tag_to_reading_tip(self, tip_id, tag_id):
        """Add tags to a reading tip
        """

        return self._tip_tags_repository.add_tag_to_reading_tip(tip_id, tag_id)

    def check_if_tag_added_to_tip(self, tip_id, tag_id):
        """Check if tag is already linked to reading tip
        """

        return self._tip_tags_repository.check_if_tag_added_to_tip(tip_id, tag_id)

    def get_all_tip_tag_pairs(self):
        """Get all tip tag pairs
        """

        return self._tip_tags_repository.get_all_tip_tag_pairs()

    def get_all_reading_tips_with_tag_id(self, tag_id):
        tip_ids = self._tip_tags_repository.get_all_reading_tip_ids_with_tag_id(tag_id)
        
        reading_tips = []
        for tip_id in tip_ids:
            reading_tips.append(self._tips_service.get_by_id(tip_id))
        
        return reading_tips

    def get_all_tags_with_tip_id(self, tip_id):
        tag_ids = self._tip_tags_repository.get_all_tag_ids_with_tip_id(tip_id)
        tags = []
        for tag_id in tag_ids:
            tags.append(self._tags_service.get_by_id(tag_id))

        return tags

    def get_all_tags_for_multiple_ids(self, tip_ids):
        """Get all tags for multiple ids
        """

        all_tags = []
        for tip_id in tip_ids:
            all_tags.append(self.get_all_tags_with_tip_id(tip_id))

        return all_tags
