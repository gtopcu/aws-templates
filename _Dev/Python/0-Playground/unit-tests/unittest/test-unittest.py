#https://www.youtube.com/watch?v=K1HSk2qZ934
#python3 -m unittest

from myclass import MyClass
import unittest

class MyClassTester(unittest.TestCase):

    def __init__(self):
        print("Constructor ran")

    def setUp(self) -> None:
        self.myclass = MyClass()
        self.myclass.add("Gokhan", 5555621966)
        self.myclass.add("Nurhan", 5055952472)
        print(self.myclass.lookup("Gokhan"))

    def test_lookup_entry(self):
        self.myclass.add("Ali", "123")
        self.assertEqual(self.myclass.lookup("Ali"), 1234)





