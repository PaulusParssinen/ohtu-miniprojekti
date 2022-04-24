import unittest
import io
import sys
from ui.console_io import ConsoleIO

class TestConsoleIO(unittest.TestCase):
    def setUp(self):
        self.io = ConsoleIO()

    def test_read(self):
        pass

    def test_write(self):
        output = io.StringIO()
        sys.stdout = output

        self.io.write("Output")

        self.assertEqual(output.getvalue(), "Output\n")
