import unittest
from src.freq import find_most_frequent_word

class TestFindMostFrequentWord(unittest.TestCase):
    def test_empty_text(self):
        self.assertEqual(find_most_frequent_word(""), "")

    def test_single_word(self):
        self.assertEqual(find_most_frequent_word("apple"), "apple")

    def test_multi_words(self):
        self.assertEqual(find_most_frequent_word("banana orange banana"), "banana")

    def test_tie(self):
        result = find_most_frequent_word("cat dog cat dog")
        self.assertIn(result, ["cat", "dog"])

    def test_case_insensitivity(self):
        self.assertEqual(find_most_frequent_word("Tree tree TREE"), "tree")


if __name__ == "__main__":
    unittest.main()
