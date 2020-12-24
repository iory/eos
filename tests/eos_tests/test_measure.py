import unittest

from eos import measure


class TestMeasure(unittest.TestCase):

    def test_measure(self):
        with measure('measure test'):
            pass
