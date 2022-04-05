class App:
    def __init__(self, reading_tip_service, io):
        self.io = io
        self.reading_tip_service = reading_tip_service

    def run(self):

        self.io.write('Welcome to Reading Tip software!\n')
        self.io.write('Choose from the following operations:\n')
        self.io.write('1. Add a Reading Tip\n')
        self.io.write('2. Modify a Reading Tip\n')
        self.io.write('3. Delete a Reading Tip\n')
        self.io.write('4. See all Reading Tips\n')
        self.io.write('5. Search Reading Tips by title\n')
        self.io.write('6. Exit software\n')

        while True:
            command = self.io.read("Select the operation you want to run (numbers only): ")
            if command == "1":

                try:
                    self.reading_tip_service.create_reading_tip() 
                    self.io.write("\nNew Reading Tip added to database.\n")
                except Exception as error:
                    self.io.write(str(error))

            elif command == "2":

                try:
                    tip_id = self.io.read('Which reading tip you want to modify? Please give id: \n')
                    reading_tip = self.reading_tip_service.validate_reading_tip(tip_id)

                    if reading_tip is False:
                        self.io.write(f"Reading tip with tip id {tip_id} was not found.")
                    else:
                        self.io.write(f"Reading tip with tip id {tip_id} found.\n")

                        self.io.write(f"Title: {reading_tip[1]}")
                        self.io.write(f"Author: {reading_tip[2]}")
                        self.io.write(f"Url: {reading_tip[3]}")

                        new_title = self.io.read('\nEnter new title:\n')
                        self.reading_tip_service.modify_reading_tip(tip_id, new_title)

                        self.io.write(f"Modification done successfully.")

                except Exception as error:
                    self.io.write(str(error))

            elif command == "3":
                try:
                    tip_id = self.io.read('Which reading tip you want to delete? Please give id.')
                except:
                    self.io.write("Invalid reading tip id")
                self.reading_tip_service.delete_reading_tip_by_id(tip_id)

            elif command == "4":
                self.reading_tip_service.see_all_reading_tips()
            
            elif command == "5":
                title = self.io.read("Enter title to search: ")
                self.reading_tip_service.search_reading_tip_by_title(title)

            elif command == "6":
                self.io.write("\nSession ended.\n")
                break