#https://www.youtube.com/watch?v=K1HSk2qZ934
#python3 -m pytest

from myclass import MyClass

def test_lookup():
    myclass = MyClass()
    myclass.add("Ali", 123)
    assert "1234" == myclass.lookup("Ali")


