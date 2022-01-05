# https://python-course.eu/python-tutorial/modules-and-modular-programming.php

import math, random
from math import sin, pi

from math import *
sin(3.01) + tan(cos(2.1)) + e

import math as mathematics
print(mathematics.cos(mathematics.pi))

#import numpy as np
#np.diag([3, 11, 7, 9])

# List module content
import math
print(dir(math))

# List buil-in functions
import builtins
print(dir(builtins))

# There are different kind of modules:
#   1. Those written in Python - they have the suffix: .py
#   2. Dynamically linked C modules - suffixes are: .dll, .pyd, .so, .sl, ...
#   3. C-Modules linked with the Interpreter
#
# It's possible to get a complete list of these modules:
import sys
print(sys.builtin_module_names)


"""
Module Search Path
If you import a module, let's say "import xyz", the interpreter searches for this module in the following locations and in the order given:

The directory of the top-level file, i.e. the file being executed.
The directories of PYTHONPATH, if this global environment variable of your operating system is set.
standard installation path Linux/Unix e.g. in /usr/lib/python3.5. 
It's possible to find out where a module is located after it has been imported:

import numpy
numpy.file
'/usr/lib/python3/dist-packages/numpy/init.py'
import random random.file '/usr/lib/python3.5/random.py'

The file attribute doesn't always exist. This is the case with modules which are statically linked C libraries.

import math
math.__file__
OUTPUT:
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-4-bb98ec32d2a8> in <module>
      1 import math
----> 2 math.__file__
AttributeError: module 'math' has no attribute '__file__'


Content of a Module
With the built-in function dir() and the name of the module as an argument, you can list all valid attributes and methods for that module.

import math
dir(math)
OUTPUT:
['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'copysign', 'cos', 'cosh', 'degrees', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'pi', 'pow', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc']
Calling dir() without an argument, a list with the names in the current local scope is returned:

import math
cities = ["New York", "Toronto", "Berlin", "Washington", "Amsterdam", "Hamburg"]
dir()
OUTPUT:
['In, 'Out, '_, '_1, '__, '___, '__builtin__, '__builtins__, '__doc__, '__loader__, '__name__, '__package__, '__spec__, '_dh, '_i, '_i1, '_i2, '_ih, '_ii, '_iii, '_oh, 'builtins, 'cities, 'exit, 'get_ipython, 'math, 'quit']
It's possible to get a list of the Built-in functions, exceptions, and other objects by importing the builtins module:

import builtins
dir(builtins)

"""