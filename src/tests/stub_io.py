import colorama
from colorama import Fore, Back, Style

class StubIO:
    def __init__(self, inputs=None):
        self.inputs = inputs or []
        self.outputs = []

    def write(self, value):
        self.outputs.append(value)

    def read(self, prompt):
        if len(self.inputs) > 0:
            return self.inputs.pop(0)
        return ""

    def add_input(self, value):
        self.inputs.append(value)

    def write_green(self, value, end='\n'):
        self.outputs.append(value)

    def write_red(self, value, end='\n'):
        self.outputs.append(value)