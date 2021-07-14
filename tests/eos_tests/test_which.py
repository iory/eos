import unittest

from eos import which


class TestWhich(unittest.TestCase):

    def test_which(self):
        self.assertNotEqual(which('python'), None)
        self.assertEqual(which('-'), None)
