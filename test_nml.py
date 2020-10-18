from pytest import approx
from read_namelist import read_namelist


FILE = "example.nml"


def test_base():
    dat = read_namelist(FILE, "base")
    assert dat["x"] == approx([1, 2, 3])

    dat = read_namelist(FILE, "empty")
    assert not dat, "empty namelist should be empty"
