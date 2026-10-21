import unittest

from greet import greet


class GreetTest(unittest.TestCase):
    def test_greet(self):
        self.assertEqual(greet("太郎"), "こんにちは、太郎さん")

    def test_greet_lower(self):
        self.assertEqual(greet("Taro", lower=True), "こんにちは、taroさん")
        self.assertEqual(greet("Taro"), "こんにちは、Taroさん")

    def test_greet_shout(self):
        self.assertEqual(greet("太郎", shout=True), "こんにちは、太郎さん！")

    def test_greet_lower_and_shout(self):
        self.assertEqual(greet("Taro", lower=True, shout=True), "こんにちは、taroさん！")

    def test_greet_name_first(self):
        self.assertEqual(greet("太郎", name_first=True), "太郎さん、こんにちは")
        self.assertEqual(greet("太郎", name_first=True, shout=True), "太郎さん、こんにちは！")
        self.assertEqual(greet("Taro", name_first=True, lower=True), "taroさん、こんにちは")


if __name__ == "__main__":
    unittest.main()
