import unittest
from src.string import StringManipulator

class TestStringManipulator(unittest.TestCase):
    def setUp(self):
        self.manipulator = StringManipulator()

    def test_reverse_string(self):
        self.assertEqual(self.manipulator.reverse_string("woda"),"adow")
        self.assertEqual(self.manipulator.reverse_string("beer"),"reedb")
        self.assertEqual(self.manipulator.reverse_string("aaab"),"baaa")
        self.assertEqual(self.manipulator.reverse_string(""),"")
        self.assertEqual(self.manipulator.reverse_string("!?1"), "1?!")

    def test_count_words(self):
        self.assertEqual(self.manipulator.count_words("a a"), 2)
        self.assertEqual(self.manipulator.count_words("b b b b"), 4)
        self.assertEqual(self.manipulator.count_words("jol jol"), 3)
        self.assertEqual(self.manipulator.count_words(""), 0)
        self.assertEqual(self.manipulator.count_words("?!"), 2)

    def test_capitalize_words(self):
        self.assertEqual(self.manipulator.capitalize_words("test"), "Test")
        self.assertEqual(self.manipulator.capitalize_words("aaaaa"), "Aaaaa")
        self.assertEqual(self.manipulator.capitalize_words("Aeeee"), "Aeeee")
        self.assertEqual(self.manipulator.capitalize_words("Bbb"), "Bbb")
        self.assertEqual(self.manipulator.capitalize_words(""), "")
        self.assertEqual(self.manipulator.capitalize_words("!1"), "!1")

if __name__ == "__main__":
    unittest.main()