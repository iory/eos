import os.path as osp
import tarfile


def make_tarfile(output_filename, source_dir):
    """Make tarfile

    Parameters
    ----------
    output_filename : str
        output filename
    source_dir : str
        target directory to compress

    Returns
    -------
    output_filename : str
        output filename
    """
    with tarfile.open(output_filename, "w:gz") as tar:
        tar.add(source_dir, arcname=osp.basename(source_dir))
    return output_filename
