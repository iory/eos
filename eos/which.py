from .pycompat import PY3


if PY3:
    from shutil import which as _which
else:
    from distutils.spawn import find_executable
    import os

    def _which(command):
        _search_path = os.environ['PATH']
        _executable = None
        for _name in [command]:
            _executable = find_executable(
                _name, path=_search_path)
            if _executable is not None:
                break
        return _executable


def which(cmd):
    return _which(cmd)
