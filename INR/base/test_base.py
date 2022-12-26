import unittest

class TestFileName(unittest.TestCase):

    def test_file_name(self):
        print("---------base---------------")
        self.assertIn("test_", __file__)