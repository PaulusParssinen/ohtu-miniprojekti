from repositories.tip_tags_repository import (
    TipTagsRepository as default_tip_tags_repository
    )

from entities.reading_tip import ReadingTip

class TipTagsService:
    def __init__(self, tip_tags_repository=default_tip_tags_repository):
        self._tip_tags_repository = tip_tags_repository

    def add_tag_to_reading_tip(self, tip_id, tag_id):
        return self._tip_tags_repository.add_tag_to_reading_tip(tip_id, tag_id)

    def check_if_tag_added_to_tip(self, tip_id, tag_id):
        return self._tip_tags_repository.check_if_tag_added_to_tip(tip_id, tag_id)

    def get_all_tip_tag_pairs(self):
        return self._tip_tags_repository.get_all_tip_tag_pairs()

    def get_all_reading_tips_with_tag_id(self, tag_id):
        reading_tips = self._tip_tags_repository.get_all_reading_tips_with_tag_id(tag_id)
        reading_tip_objects = []
        for reading_tip in reading_tips:
            identifier, title, url = reading_tip[0], reading_tip[1], reading_tip[5]
            reading_tip_object = ReadingTip(identifier=identifier, title=title, url=url)
            reading_tip_objects.append(reading_tip_object)
        return reading_tip_objects

    def get_all_tags_with_tip_id(self, tip_id):

        tags = self._tip_tags_repository.get_all_tags_with_tip_id(tip_id)
        tag_names = []
        for tag in tags:
            tag_name = tag[1]
            tag_names.append(tag_name)

        return tag_names

    def get_all_tags_for_multiple_ids(self, tip_ids):
        all_tags = []

        for tip_id in tip_ids:
            tags = self.get_all_tags_with_tip_id(tip_id)
            all_tags.append(tags)

        return all_tags
