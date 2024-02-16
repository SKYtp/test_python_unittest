import unittest

import app

class AppTestCase(unittest.TestCase):
    def test_add(self):
        # test hello
        res = app.add(1, 2)
        self.assertEqual(res, 3)

if __name__ == "__main__":
    unittest.main()
