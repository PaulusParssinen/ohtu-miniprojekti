from entities.reading_tip import ReadingTip

class ReadingTipService:
    def __init__(self, reading_tip_repository=None):
        self._reading_tip_repository = reading_tip_repository
    
    def create_reading_tip(self):
        #self._reading_tip_repository.create(ReadingTip())
        print("Testataan create_reading_tip")

    def remove_reading_tip(self):
        #self._reading_tip_repository.remove(ReadingTip())
        print("Testataan remove_reading_tip")

    def search_reading_tip(self):
        pass

    def modify_reading_tip(self):
        print("Testataan modify_reading_tip")
