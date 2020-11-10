# Fortran Namelist Reader

[![Build Status](https://dev.azure.com/mhirsch0512/fortran-namelist/_apis/build/status/scivision.fortran-namelist?branchName=master)](https://dev.azure.com/mhirsch0512/fortran-namelist/_build/latest?definitionId=23&branchName=master)
![ci](https://github.com/scivision/fortran-namelist/workflows/ci/badge.svg)

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

## Examples

[read.f90](./read.f90)
example shows that one must allocate arrays before reading a namelist array variable.
Character can be read with a variable (much) longer than known needed, then trim() to another allocatable character variable.
Despite what some forums say, reading namelist directly into allocatable just segfaults with Intel or GCC compilers.
