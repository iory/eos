import os
import shutil
import tempfile
import unittest

from eos import makedirs
from eos import run_many


class TestRunMany(unittest.TestCase):

    def test_run_many(self):
        _, dirname = tempfile.mkstemp()
        os.remove(dirname)
        makedirs(dirname)
        cmd = """
        python -c 'from eos import make_fancy_output_dir; \
        make_fancy_output_dir(\"""" + dirname + """\")'"""
        run_many(cmd, 8, jobs=2, sleep_time=0.0)
        shutil.rmtree(dirname)
