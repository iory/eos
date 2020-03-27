import argparse
import datetime
import json
import os
import socket
import sys
import tempfile


def make_fancy_output_dir(dirname=None,
                          args=None,
                          time_format='%Y-%m-%d-%H-%M-%S-%f',
                          dir_suffix_name='',
                          save_environ=True,
                          save_command=True,
                          save_gitignore=True):
    """Create fancy output directory.

    Parameters
    ----------
    dirname : str or None
        if this is None, create tmporary directory.
    args : argparse.Namespace or None
        if args is specified, dump args to created directory.
    time_format : str
        time format.
    dir_suffix_name : str
        suffix name of directory
    save_environ : bool
        if True, dump environemnt values to environ.txt.
    save_command : bool
        if True, dump input command value to command.txt.
    save_gitignore : bool
        if True, add gitignore to output directory.
    Returns
    -------
    outdir : str
        path of created directory.

    Examples
    --------
    >>> from eos import make_fancy_output_dir
    >>> make_fancy_output_dir('/tmp/results')
    '/tmp/results/iory-mac-2020-03-27-18-52-49-215104-67099'
    """
    time_str = datetime.datetime.now().strftime(time_format)
    time_str = socket.gethostname() + '-' + time_str + '-' + str(os.getpid())
    time_str += dir_suffix_name
    if dirname is not None:
        # create directory
        if os.path.exists(dirname):
            if not os.path.isdir(dirname):
                raise RuntimeError(
                    '{} is not a directory'.format(dirname))
        outdir = os.path.join(dirname, time_str)
        if os.path.exists(outdir):
            raise RuntimeError('{} exists'.format(outdir))
        else:
            os.makedirs(outdir)
    else:
        outdir = tempfile.mkdtemp(prefix=time_str)

    if args is not None:
        # Save all the arguments
        with open(os.path.join(outdir, 'args.txt'), 'w') as f:
            if isinstance(args, argparse.Namespace):
                args = vars(args)
            f.write(json.dumps(args))
            f.write('\n')

    if save_environ:
        # Save all the environment variables
        with open(os.path.join(outdir, 'environ.txt'), 'w') as f:
            f.write(json.dumps(dict(os.environ),
                               ensure_ascii=False,
                               indent=4))
            f.write('\n')

    if save_command:
        # Save the command
        with open(os.path.join(outdir, 'command.txt'), 'w') as f:
            f.write(' '.join(sys.argv))
            f.write('\n')

    if save_gitignore:
        with open(os.path.join(outdir, '.gitignore'), 'w') as f:
            f.write('*\n')

    return outdir
