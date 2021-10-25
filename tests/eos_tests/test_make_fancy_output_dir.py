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

        # exist ok
        output_dir = make_fancy_output_dir(
            target_dir,
            time_format=None,
            exist_ok=True)
        with self.assertRaises(RuntimeError):
            output_dir = make_fancy_output_dir(
                target_dir,
                time_format=None,
                exist_ok=False)

        target_dir = osp.join(dirname, 'result')
        output_dir = make_fancy_output_dir(
            target_dir,
            no_save=True)
        self.assertEqual(
            osp.exists(osp.join(output_dir, 'args.txt')), False)
        self.assertEqual(
            osp.exists(osp.join(output_dir, 'environ.txt')), False)
        self.assertEqual(
            osp.exists(osp.join(output_dir, 'pip-freeze.txt')), False)

        # clean test directory
        shutil.rmtree(dirname)
