# Fortran Namelist Reader

Pure Python and Matlab **readers** for
[Fortran namelist](https://github.com/scivision/fortran2018-examples/tree/master/namelist)
=> dict / struct

These are as basic as possible, for putting in your own program directly.
They output dict (Python) or struct (Matlab).

Consider
[f90nml](https://github.com/marshallward/f90nml)
for a full-featured read/write Fortran namelist Python package.

## Python

```python
from read_namelist import read_namelist

print(read_namelist('example.nml', 'base'))
```

## Matlab

```octave
read_namelist('example.nml', 'base')
```
