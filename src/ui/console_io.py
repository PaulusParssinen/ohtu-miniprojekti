import colorama
from colorama import Fore, Back, Style

class ConsoleIO:

    def write(self, value, end='\n'):
        print(value, end=end)

    def write_green(self, value, end='\n'):
        print(Fore.GREEN+value+Style.RESET_ALL, end=end)

    def write_red(self, value, end='\n'):
        print(Fore.RED+value+Style.RESET_ALL, end=end)

    def read(self, prompt):
        return input(prompt)
