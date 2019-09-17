# Fortran Namelist Reader

Pure Python (read_nml.py) and Matlab (read_nml_group.m) **readers** for
[Fortran namelist](https://github.com/scivision/fortran2018-examples/tree/master/namelist) => dict / struct

These are as basic as possble, for putting in your own program directly.
Consider [f90nml](https://github.com/marshallward/f90nml) for a full-featured read/write Fortran namelist package.

## Python

```python
from read_nml import read_nml_group

print(read_nml_group('example.nml', 'base'))
```

## Matlab

```octave
read_nml_group('example.nml', 'base')
```
