import datetime


def current_time_str(time_format='%Y-%m-%d-%H-%M-%S-%f'):
    time_str = datetime.datetime.now().strftime(time_format)
    return time_str
