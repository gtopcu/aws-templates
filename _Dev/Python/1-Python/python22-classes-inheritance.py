
# https://www.w3schools.com/python/python_classes.asp

class MyClass:
  x = 5

p1 = MyClass()
print(p1.x)

# The self parameter is a reference to the current instance. Can have any name, must be first arg 
# of the class, and is used to access variables that belong to the class (like Java - this)
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.age = 40
p1.myfunc()

# Deleting object property & object
del p1.age
del p1

# Inheritance
class Student(Person):
  pass

st = Student("John", 36)
st.age = 40
st.myfunc()

# Override parent's super
class Student(Person):
  def __init__(self, fname, lname):
    city = "Ist"

# Use parent's super:
class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)

# super() function that will make the child class inherit all the methods and properties from its parent:
class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)

# Add a property called graduationyear to the Student class:
class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
    self.graduationyear = 2019

  # Add a year parameter, and pass the correct year when creating objects:
  class Student(Person):
    def __init__(self, fname, lname, year):
      super().__init__(fname, lname)
      self.graduationyear = year

x = Student("Mike", "Olsen", 2019)

# Add a method called welcome to the Student class
# If you add a method in the child class with the same name as a function in the parent class, 
# the inheritance of the parent method will be overridden.
class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)
