import os

from paths import Paths

"""The Paths class may need additional attributes, so just test on one
existing one rather than forcing all paths to be given to the constructor.
This will lead to tightly coupled tests."""

def test_local():
    Paths.timeout = ["hello", "mate.py"]
    p = Paths()
    os.environ["REACT_APP_HOST"] = "LOCAL"
    assert p.timeout == f"hello{os.path.sep}mate.py"

def test_remote():
    Paths.timeout = ["hello", "mate.py"]
    p = Paths()
    os.environ["REACT_APP_HOST"] = "REMOTE"
    assert p.timeout == f"focus-tracker{os.path.sep}hello{os.path.sep}mate.py"
