import os
import os.path as osp
import shutil
import tempfile
import unittest

from eos import makedirs


class TestMakedirs(unittest.TestCase):

    def test_makedirs(self):
        # create test directory
        _, dirname = tempfile.mkstemp()
        os.remove(dirname)
        makedirs(dirname)

        target_dir = osp.join(dirname, 'test_makedirs')
        makedirs(target_dir)
        makedirs(target_dir, exist_ok=True)
        with self.assertRaises(OSError):
            makedirs(target_dir, exist_ok=False)

        target_dir = osp.join(dirname, 'test_makedirs', '1', '2')
        makedirs(target_dir)
        makedirs(target_dir, exist_ok=True)
        with self.assertRaises(OSError):
            makedirs(target_dir, exist_ok=False)

        # clean test directory
        shutil.rmtree(dirname)
