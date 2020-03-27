# eos: Extended os module

## Install

```
pip install extendedos
```

## Quick Start

```
>>> import os.path as osp
>>> from eos import makedirs
>>> makedirs('/tmp/example/1/2')
>>> osp.exists('/tmp/example/1/2')
True
>>> from eos import make_fancy_output_dir
>>> make_fancy_output_dir('/tmp/result')
'/tmp/result/iory-mac-2020-03-27-19-08-17-191116-46504'
```
