import unittest

from greet import greet


class GreetTest(unittest.TestCase):
    def test_greet(self):
        self.assertEqual(greet("太郎"), "こんにちは、太郎さん")

    def test_greet_lower(self):
        self.assertEqual(greet("Taro", lower=True), "こんにちは、taroさん")
        self.assertEqual(greet("Taro"), "こんにちは、Taroさん")


if __name__ == "__main__":
    unittest.main()
