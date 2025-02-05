tquiet
======

[![Last release](https://img.shields.io/pypi/v/tquiet.svg)](https://pypi.python.org/pypi/tquiet)
[![Python version](https://img.shields.io/pypi/pyversions/tquiet.svg)](https://pypi.python.org/pypi/tquiet)
[![Documentation](https://img.shields.io/readthedocs/tquiet.svg)](https://tquiet.readthedocs.io/en/latest/)
[![Test status](https://img.shields.io/github/actions/workflow/status/kalekundert/tquiet/test.yml?branch=master)](https://github.com/kalekundert/tquiet/actions)
[![Test coverage](https://img.shields.io/codecov/c/github/kalekundert/tquiet)](https://app.codecov.io/github/kalekundert/tquiet)
[![Last commit](https://img.shields.io/github/last-commit/kalekundert/tquiet?logo=github)](https://github.com/kalekundert/tquiet)

This library provides a class that mimics the `tqdm` API, but that doesn't 
actually display a progress bar.  The idea is that this can be a default 
argument to functions with long-running loops.  That way, the caller can 
control whether or not to display a progress bar.
