import os


def actual_file():
    """
    The actual current file [/home/jscul/Software/common/common.py/os].
    """

    return os.path.dirname(os.path.abspath(__file__))


def working_directory():
    """
    Workspace root [/home/jscul/Software/common/common.py].
    """

    return os.getcwd()


if __name__ == "__main__":

    print(actual_file())
    print(working_directory())
