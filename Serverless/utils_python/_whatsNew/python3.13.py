
# https://www.python.org/downloads/

# ************************************************************************************
# Python 3.13 - 2024-10-07
# https://www.python.org/downloads/release/python-3130/
# https://www.youtube.com/watch?v=eUDGlxu_-ic
# ************************************************************************************

# 1. Improved interpreter output & errors
# 2. (Exp) Free-threaded version of CPython - no Global Interpreter Lock, can now be disabled
# 3. (Exp) JIT compilator
# 4. TypedDict got ReadOnly attributes
# 5. from math import fma added - Fused multiply-add operation. Computes (x * y) + z with a single round.
# 6. from pathlib import Path can now use file URIs such as path = Path('file:///usr/bin')
# 7. from re import PatternError added for pattern errors specificially
# 8. from typing import is_protocol added
# 9. random package now has CLI support
# 10. time package now has better precision for Windows - lower than 1 microsecond
# 11. Improved garbage collection - almost no pauses, works better for circular references, groups short-lived and others
# 12.
#   from warnings import deprecated
#         @deprecated("Use B instead")  
#             class A:  
#                 pass 
# 
# 13. Classes now have __static_attributes__ dunder attribute as tuple. Superclasses are not included
#   class MyClass:
#       def __init__(self) -> None:
#           self.a = 1
#           self.b = 2
#   print(MyClass.__static_attributes__) # prints ('a', 'b')
# 
# 14. IOS is now PEP11 supported platform - iPhone & iPad. Andriod support is also coming (PEP738)













# ************************************************************************************
# ************************************************************************************

