# Asserts

[![Build Status](https://travis-ci.org/Dimrok/asserts.svg?branch=master)](https://travis-ci.org/Dimrok/asserts)

A simple library glorifying python3 assert in many ways.

## Examples

```python3
>>> from asserts import *
>>> assertIn(3, [1, 2, 3])
>>>
>>> assertIn(5, [1, 2, 3])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<...>/asserts/__init__.py", line 3, in assertIn
    raise AssertionError('{} not in {}'.format(v, c))
AssertionError: 5 not in [1, 2, 3]
>>>
>>> assertLt(4, 3)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<...>/asserts/__init__.py", line 27, in assertLt
    raise AssertionError('{} >= {}'.format(l, r))
AssertionError: 4 >= 3
>>>
```

## Functions

- assertIn
- assertNin
- assertEq
- assertNeq
- assertGt
- assertGe
- assertLt
- assertLe
- assertIsInstance
- assertNisInstance
- assertThrow
- assertNoThrow

## Tests

Tests are embeded in the file. To test it, run: `python3 __init__.py`.
