class App:
    def __init__(self, reading_tip_service, io):
        self.io = io
        self.reading_tip_service = reading_tip_service
    
    def run(self):

        self.io.write('Welcome to Reading Tip software!\n')
        self.io.write('Choose from the following operations:\n 1. Add a reading tip\n 2. Exit software\n')

        while True:
            command = self.io.read("Select the operation you want to run (numbers only): ")
            if command == "1":

                try:
                    self.reading_tip_service.create_reading_tip()
                    self.io.write("\nNew Reading Tip added to database.\n")
                except Exception as error:
                    self.io.write(str(error))

            elif command == "2":
                self.io.write("\nSession ended.\n")
                break
        
        

        
        

        

