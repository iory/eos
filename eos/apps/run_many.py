#!/usr/bin/env python

import argparse
from argparse import RawTextHelpFormatter

from eos import run_many


def main():
    parser = argparse.ArgumentParser(
        formatter_class=RawTextHelpFormatter,
        description='Execute command multiple times.\n\n'
        'Examples\n'
        '--------\n'
        'run-many "python -c \'import os; print(os.getpid())\'" '
        '-n 8 --jobs 2 --sleep-time 0.1 --verbose')
    parser.add_argument('cmd', type=str,
                        help='Input command.')
    parser.add_argument('--jobs', '-j', type=int, default=16,
                        help='Number of parallel process')
    parser.add_argument('--num', '-n', type=int, default=32,
                        help='Number of commands to execute.')
    parser.add_argument('--sleep-time', type=float, default=1.0,
                        help='Sleep interval.')
    parser.add_argument('--verbose', action='store_true',
                        help='Print information')
    args = parser.parse_args()
    run_many(args.cmd, args.num, jobs=args.jobs,
             sleep_time=args.sleep_time, verbose=args.verbose)


if __name__ == '__main__':
    main()
