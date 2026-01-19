import unittest
from main import is_palindrome


class TestIsPalindrome(unittest.TestCase):

    def test_palindrome_words(self):
        self.assertTrue(is_palindrome("level"))
        self.assertTrue(is_palindrome("Madam"))
        self.assertTrue(is_palindrome("Radar"))

    def test_not_palindrome_words(self):
        self.assertFalse(is_palindrome("hello"))
        self.assertFalse(is_palindrome("Python"))

    def test_empty_string(self):
        self.assertTrue(is_palindrome(""))


if __name__ == "__main__":
    unittest.main()
