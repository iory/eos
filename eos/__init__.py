# flake8: noqa

import pkg_resources


__version__ = pkg_resources.get_distribution("eos").version


from eos.makedirs import makedirs
