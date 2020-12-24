import contextlib
import datetime as datetime_module
import sys


if sys.version_info[:2] >= (3, 6):
    time_isoformat = datetime_module.time.isoformat
else:
    def time_isoformat(time, timespec='microseconds'):
        assert isinstance(time, datetime_module.time)
        if timespec != 'microseconds':
            raise NotImplementedError
        result = '{:02d}:{:02d}:{:02d}.{:06d}'.format(
            time.hour, time.minute, time.second, time.microsecond
        )
        assert len(result) == 15
        return result


if sys.version_info[:2] >= (3, 7):
    time_fromisoformat = datetime_module.time.fromisoformat
else:
    def time_fromisoformat(isoformat_str):
        hour, minute, second, microsecond = map(
            int,
            isoformat_str.replace('.', ':').split(':'))
        return datetime_module.time(hour, minute, second, microsecond)


def timedelta_isoformat(timedelta, timespec='microseconds'):
    time = (datetime_module.datetime.min + timedelta).time()
    return time_isoformat(time, timespec)


@contextlib.contextmanager
def measure(log_name='Total elapsed time',
            file=sys.stderr):
    """Measure time with contextlib.

    Parameters
    ----------
    log_name : str
        log name
    file : writable object
        writable object such as sys.stderr.

    Examples
    --------
    >>> from eos import measure
    >>> with measure('measure example'):
    ...     time.sleep(2.0)
    measure example: 00:00:02.002104
    """
    start_time = datetime_module.datetime.now()
    yield
    duration = datetime_module.datetime.now() - start_time
    now_string = timedelta_isoformat(duration)
    file.write('{log_name}: {now_string}\n'.format(
        **locals()))
