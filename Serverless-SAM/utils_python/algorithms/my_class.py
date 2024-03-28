
class MyClass:
    
    cls_var: str = "Class variable"

    def __init__(self, name: str = ""):
        self.name: str = name
        self._age: int = 0
    def get_name(self) -> str:
        return self.name
    def format_name(self) -> str:
        return self.get_name().casefold()

    @property
    def age(self):
        return self._age
    @age.setter
    def set_age(self, age: int):
        self._age = age
        return self._age
    @age.deleter
    def del_age(self):
        del self._age
        return self._age

    @classmethod
    def get_cls_var(cls):
        return cls.cls_var

    @staticmethod
    def static_method():
        print("STATIC")


cls = MyClass("John")
print(cls.get_name())
print(cls.format_name())
MyClass.static_method()

