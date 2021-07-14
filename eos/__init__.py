# flake8: noqa

import pkg_resources


__version__ = pkg_resources.get_distribution("extendedos").version


from eos.compress import make_tarfile
from eos.make_fancy_output_dir import make_fancy_output_dir
from eos.makedirs import makedirs
from eos.measure import measure
from eos.run_many import run_many
from eos.time_str import current_time_str
from eos.which import which
