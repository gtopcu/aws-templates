
# https://www.tutorialsteacher.com/python/classmethod-decorator

# class Student:
    
#     name = 'unknown' #class attribute

#     def __init__(self, name):
#         self.__name = name #instance attribute

#     @property
#     def name(self):
#         return self.__name
    
#     @name.setter
#     def name(self, value):
#         self.__name=value
    
#     @name.deleter
#     def name(self):
#         print('Deleting..')
#         del self.__name

#     @classmethod
#     def tostring(cls):
#         print('Student Class Attributes: name=', cls.name)

#     @classmethod
#     def getobject(cls):
#         return cls('Steve')
        
# std = Student('Steve')
# del std.name
# print(std.name)  #AttributeError

# Student.tostring()  #Student Class Attributes: name=unknown
# std = Student.getobject()
# print(std.name)  #'Steve' 


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

