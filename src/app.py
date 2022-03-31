class App:
    def __init__(self, io):
        self.io = io
    
    def run(self):

        self.io.write('Welcome to Reading Tip software!\n')
        self.io.write("Choose from the following operations:\n 1. Add a reading tip\n 2. Exit software\n")

        while True:
            command = self.io.read("Select the operation you want to run (numbers only): ")
            if command == "1":
                self.io.write("\nlisätään kantaan\n")
            elif command == "2":
                self.io.write("\nSession ended.\n")
                break

        
        

        

