import os
import os.path as osp
import shutil
import tempfile
import unittest

from eos import make_fancy_output_dir
from eos import make_tarfile
from eos import makedirs


class TestCompress(unittest.TestCase):

    def test_make_tarfile(self):
        # create test directory
        _, dirname = tempfile.mkstemp()
        os.remove(dirname)
        makedirs(dirname)

        target_dir = osp.join(dirname, 'result')
        output_dir = make_fancy_output_dir(target_dir)
        tar_filename = '{}.tar.gz'.format(output_dir)
        make_tarfile(tar_filename, output_dir)
        self.assertEqual(osp.exists(tar_filename), True)

        # clean test directory
        shutil.rmtree(dirname)
