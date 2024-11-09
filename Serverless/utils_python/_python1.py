
####################################################################################################

# https://docs.python.org/3/library/enum.html
# from enum import Enum, auto, IntEnum, StrEnum, IntFlag
# class Color(Enum):
#     RED = 1
#     GREEN = 2
#     BLUE = 3
#   def __str__(self):
#       return self.value
#   def __repr__(self):
#       return "<%s.%s>" % (self.__class__.__name__, self._name_)

# # functional syntax
# # Color = Enum('Color', ['RED', 'GREEN', 'BLUE'])

# python(str, Enum)

# class Role(IntEnum): # IntFlag
#     AUTHOR = auto() # object()
#     EDITOR = auto()
#     VIEWER = auto()
#     ADMIN = AUTHOR | EDITOR | VIEWER

# class StringEnum(StrEnum):
#     str1 = "str1"
#     str2 = "str2"

####################################################################################################
# Multiple Except

# def main() -> None:
#     try:
#         x = 0 / 3
#         print("Division: " + x)
#     except (KeyError, ValueError) as e:
#        print(e)
    
####################################################################################################

# class MyContextManager():

#     def __enter__(self):
#         lock.acquire()

#     def __exit__(self, exc_type, exc_val, exc_tb):
#         lock.release()

#     def isLocked():
#         return lock.locked()

####################################################################################################

