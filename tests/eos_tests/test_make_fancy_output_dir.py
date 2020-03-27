import os
import os.path as osp
import shutil
import tempfile
import unittest

from eos import make_fancy_output_dir
from eos import makedirs


class TestMakeFancyOutputDir(unittest.TestCase):

    def test_make_fancy_output_dir(self):
        # create test directory
        _, dirname = tempfile.mkstemp()
        os.remove(dirname)
        makedirs(dirname)

        target_dir = osp.join(dirname, 'result')
        output_dir = make_fancy_output_dir(target_dir)
        self.assertEqual(osp.exists(output_dir), True)

        # clean test directory
        shutil.rmtree(dirname)
