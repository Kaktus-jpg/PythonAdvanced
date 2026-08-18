import os
import unittest


class TestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.file_path = "file.txt"
        with open(self.file_path, "w", encoding="utf8") as file:
            file.write("qwerty")

    def test(self):
        with open(self.file_path, "r", encoding="utf8") as file:
            self.assertTrue(file.read())
            return file.read()

    def tearDown(self) -> None:
        os.remove(self.file_path)
