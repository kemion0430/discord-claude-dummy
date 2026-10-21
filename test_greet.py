import unittest

from greet import greet


class GreetTest(unittest.TestCase):
    def test_greet(self):
        self.assertEqual(greet("太郎"), "こんにちは、太郎さん")


if __name__ == "__main__":
    unittest.main()
