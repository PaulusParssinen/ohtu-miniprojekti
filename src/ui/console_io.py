class ConsoleIO:
    def write(self, value='', end='\n'):
        print(value, end=end)

    def read(self, prompt):
        return input(prompt)
