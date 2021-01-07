import unittest

from eos import current_time_str


class TestTimeStr(unittest.TestCase):

    def test_current_time_str(self):
        current_time_str()
