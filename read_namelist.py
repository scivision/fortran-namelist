#!/usr/bin/env python3
"""
Copyright 2019 Michael Hirsch

If you need a full Python package look at f90nml

read_namelist() reads a single namelist, returning the values in a dict()
It strips extraneous apostrophes
"""
import typing as T
import re
from pathlib import Path


def namelist_exists(fn: Path, namelist: str) -> bool:
    """ determines if a namelist exists in a file """

    pat = re.compile(r"^\s*&(" + namelist + ")$")

    with fn.open("r") as f:
        for line in f:
            if pat.match(line) is not None:
                return True

    return False


def read_namelist(fn: Path, namelist: str) -> T.Dict[str, T.Any]:
    """ read a namelist from an .nml file """

    raw: T.Dict[str, T.Sequence[str]] = {}
    nml_pat = re.compile(r"^\s*&(" + namelist + r")")
    end_pat = re.compile(r"^\s*/\s*$")
    val_pat = re.compile(r"^\s*(\w+)\s*=\s*['\"]?([^!'\"]*)['\"]?")

    fn = Path(fn).expanduser()

    with fn.open("r") as f:
        for line in f:
            if not nml_pat.match(line):
                continue

            for line in f:
                if end_pat.match(line):
                    # end of namelist
                    return parse_values(raw)
                val_mat = val_pat.match(line)
                if not val_mat:
                    continue

                key, vals = val_mat.group(1), val_mat.group(2).strip().split(",")
                raw[key] = vals[0].strip() if len(vals) == 1 else vals

    raise KeyError(f"did not find Namelist {namelist} in {fn}")


def parse_values(raw: T.Dict[str, T.Any]):
    for k, v in raw.items():
        if isinstance(v, list):
            try:
                raw[k] = list(map(float, v))
            except ValueError:
                pass
        else:
            try:
                raw[k] = float(v)
            except ValueError:
                pass

    return raw


if __name__ == "__main__":
    import argparse

    p = argparse.ArgumentParser(description="Read Fortran Namelist to Dict")
    p.add_argument("file", help=".nml file to load")
    P = p.parse_args()

    for g in ("base", "empty"):
        dat = read_namelist(P.file, g)
        print(dat)
