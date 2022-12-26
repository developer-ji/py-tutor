from base.test_base import TestFileName
print("---test-file----")
import unittest

class TestStringMethods(TestFileName):

    def test_upper(self):
        print("-------------test-upper---------")
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        print("-------------test-is-upper---------")
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        print("-------------test-split---------")
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()