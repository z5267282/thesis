import os
from paths import Paths

def test_local():
    p = Paths()
    os.environ["REACT_APP_HOST"] = "LOCAL"
    assert p.timeout == os.path.join("src", "upload", "timeout")

def test_remote():
    p = Paths()
    os.environ["REACT_APP_HOST"] = "REMOTE"
    assert p.timeout == os.path.join(
        "focus-tracker", "src", "upload", "timeout")

def test_program():
    p = Paths()
    os.environ["REACT_APP_HOST"] = "LOCAL"
    assert p.program == os.path.join("src", "program.py")

def test_sanity():
    p = Paths()
    os.environ["REACT_APP_HOST"] = "LOCAL"
    assert p.sanity == os.path.join("src", "upload", "sanity-run")

def test_generated_frame():
    p = Paths()
    os.environ["REACT_APP_HOST"] = "LOCAL"
    assert p.generated_frame == os.path.join("gen-dataframe", "generated.json")

def test_to_python():
    p = Paths()
    os.environ["REACT_APP_HOST"] = "LOCAL"
    assert p.to_python == os.path.join("gen-dataframe", "to-py")

def test_as_python():
    p = Paths()
    os.environ["REACT_APP_HOST"] = "LOCAL"
    assert p.as_python == os.path.join("gen-dataframe", "generated.py")
