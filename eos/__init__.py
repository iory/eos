# flake8: noqa

import pkg_resources


__version__ = pkg_resources.get_distribution("eos").version


from eos.make_fancy_output_dir import make_fancy_output_dir
from eos.makedirs import makedirs
