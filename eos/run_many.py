import multiprocessing
import os
import signal
import subprocess
import time


def run_many(cmd, n, jobs=None, sleep_time=1.0, verbose=True):
    """Running commands in parallel.

    Parameters
    ----------
    cmd : str
        command to execute.
    n : int
        number of commands to execute.
    jobs : None or int
        number of parallel execution. If `None`,
        automatically set min(multiprocessing.cpu_count(), n).
    sleep_time : float
        sleep time between commands to be executed.
    verbose : bool
        If `True`, print information.
    """
    if jobs is None:
        jobs = min(n, multiprocessing.cpu_count())

    if verbose:
        start = time.time()

    try:
        procs = []
        num_finish = 0
        for i in range(n):
            procs.append(subprocess.Popen(cmd, shell=True))
            time.sleep(sleep_time)
            while len(procs) >= jobs:
                for p in procs:
                    ret = p.poll()
                    if ret is not None:
                        procs.remove(p)
                        num_finish += 1
                        if verbose:
                            print("finish {} processes".format(num_finish))
                        break
                else:
                    time.sleep(sleep_time)
        while procs:
            for p in procs:
                ret = p.poll()
                if ret is not None:
                    procs.remove(p)
                    num_finish += 1
                    if verbose:
                        print("finish {}processes".format(num_finish))
                    break
            else:
                time.sleep(sleep_time)
    except KeyboardInterrupt:
        for p in procs:
            os.killpg(os.getpgid(p.pid), signal.SIGINT)

    if verbose:
        elapsed_time = time.time() - start
        print("elapsed_time: {0}".format(elapsed_time) + "[sec]")
