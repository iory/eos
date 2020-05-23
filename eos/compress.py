import os.path as osp
import tarfile


def make_tarfile(output_filename, source_dir=None):
    """Make tarfile

    Parameters
    ----------
    output_filename : str
        output filename. If source_dir is None, output_filename is considered
        as the source_dir name.
    source_dir : str or None
        target directory to compress.

    Returns
    -------
    output_filename : str
        output filename
    """
    if source_dir is None:
        source_dir = output_filename
        output_filename = "{}.tar.gz".format(source_dir)
    with tarfile.open(output_filename, "w:gz") as tar:
        tar.add(source_dir, arcname=osp.basename(source_dir))
    return output_filename
