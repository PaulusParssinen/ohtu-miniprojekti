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
        self.io.write('4. Search Reading Tips by title\n')
        self.io.write('5. Exit software\n')

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
                    self.reading_tip_service.modify_reading_tip()
                except Exception as error:
                    self.io.write(str(error))

            elif command == "3":
                try:
                    tip_id = self.io.read('Which reading tip you want to delete? Please give id.')
                except:
                    self.io.write("Invalid reading tip id")
                self.reading_tip_service.delete_reading_tip_by_id(tip_id)

            elif command == "4":
                title = self.io.read("Enter title to search: ")
                self.reading_tip_service.search_reading_tip_by_title(title)

            elif command == "5":
                self.io.write("\nSession ended.\n")
                break