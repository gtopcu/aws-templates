
import os
import sys
import json
import random

class MyClass:
        
        def __init__(self):
                self.entries = { "gn": 4123123,  "gm": 72823123 }
        
        def add(self, name: str, number: int) -> None:
                self.entries[name] = number
                #print(self.entries.keys)
        
        def lookup(self, name: str) -> int:
                return self.entries[name]
                return None
        
        def names(self) -> dict:
                return self.entries.keys()
        
        def phones(self) -> dict:
                return self.entries.values()


if __name__ == '__main__':

    #print(dir(json))
    myclass = MyClass()
    myclass.add("gt", 12345)
    for val in myclass.entries:
        print(val)
    #print(myclass.names)
    print("Ran!")

