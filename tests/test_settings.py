import logging
import sys
import unittest
from PyQt5.QtCore import Qt
from PyQt5.QtTest import QTest
from PyQt5.QtWidgets import QApplication
from src.core.tenny import Settings
from src.widget.window import MainWindow


class TestSettings(unittest.TestCase):

    def setUp(self):

        logging.basicConfig(level=logging.DEBUG,
                            format='%(levelname)s: %(message)s')
        self.window = MainWindow()

    def test_default_values(self):

        self.assertIsInstance(self.window, MainWindow)


if __name__ == '__main__':
    unittest.main()
