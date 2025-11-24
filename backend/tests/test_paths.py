import os

from paths import Paths

def test_local():
    p = Paths()
    os.environ["REACT_APP_HOST"] = "LOCAL"
    assert p.timeout == os.path.join("src", "upload", "timeout")

def test_remote():
    p = Paths()
    os.environ["REACT_APP_HOST"] = "REMOTE"
    assert p.timeout == p.timeout == os.path.join("focus-tracker", "src", "upload", "timeout")
