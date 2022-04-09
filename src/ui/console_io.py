import colorama
from colorama import Fore, Back, Style, init

init(autoreset=True)

class ConsoleIO:
    def write(self, value, end='\n'):
        print(value, end=end)

    def write_green(self, value, end='\n'):
        print(Fore.GREEN+value, end=end)

    def write_red(self, value, end='\n'):
        print(Fore.RED+value, end=end)

    def read(self, prompt):
        return input(prompt)
