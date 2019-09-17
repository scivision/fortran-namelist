#!/usr/bin/env python3
"""
Copyright 2019 Michael Hirsch, Ph.D.  https://www.scivision.dev  MIT License

If you need a full Python package look at f90nml

read_nml_group() reads a single namelist group, returning the values in a dict()
It strips extraneous apostrophes
"""
import typing
from pathlib import Path

R = Path(__file__).resolve().parents[1]


def read_nml_group(fn: Path, group: str) -> typing.Dict[str, typing.Any]:
    """ read a group from an .nml file

    returns all values as strings.

    """
    fn = Path(fn).expanduser()
    raw = {}

    with fn.open("r") as f:
        for line in f:
            if not line.lstrip().startswith(f"&{group}"):
                continue
            for line in f:
                if line.strip().startswith("/"):
                    # end of group
                    break
                vals = line.split("=")
                if len(vals) != 2:
                    # not a valid line
                    continue

                key = vals[0].strip()
                values = [v.strip().strip("\'\"") for v in vals[1].split("!")[0].split(",")]
                if len(values) == 1:
                    values = values[0]
                raw[key] = values

    if not raw:
        raise KeyError(f"did not find group {group} in {fn}")

    return raw
