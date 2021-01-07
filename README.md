# eos: Extended os module

[![Build Status](https://github.com/iory/eos/workflows/Run%20Tests/badge.svg?branch=master)](https://github.com/iory/eos/actions)

## Install

```
pip install extendedos
```

## Quick Start

```
import os.path as osp
from eos import makedirs
makedirs('/tmp/example/1/2')
osp.exists('/tmp/example/1/2')
# True
from eos import make_fancy_output_dir
make_fancy_output_dir('/tmp/result')
# '/tmp/result/iory-mac-2020-03-27-19-08-17-191116-46504'
make_fancy_output_dir(time_format=None)
# '/tmp/vm7bwis1'
```

```
from eos import measure
import time
with measure('measure_example'):
   time.sleep(1.0)
# measure_example: 00:00:01.000574
```

```
from eos import current_time_str
current_time_str()
# '2021-01-08-07-42-12-301381'
```
