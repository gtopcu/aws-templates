# https://docs.python.org/3/library/unittest.html

# python -m unittest
# python -m unittest tests/test_something.py
# python -m unittest -v test_module
# python -m unittest -h

# cd project_directory
#python -m unittest discover

"""
test fixture
A test fixture represents the preparation needed to perform one or more tests, and any associated cleanup actions. 
This may involve, for example, creating temporary or proxy databases, directories, or starting a server process.

test case
A test case is the individual unit of testing. It checks for a specific response to a particular set of inputs. 
unittest provides a base class, TestCase, which may be used to create new test cases.

test suite
A test suite is a collection of test cases, test suites, or both. It is used to aggregate tests that should be 
executed together.

test runner
A test runner is a component which orchestrates the execution of tests and provides the outcome to the user. 
The runner may use a graphical interface, a textual interface, or return a special value to indicate the results of executing the tests.
"""

import unittest

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOo'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()

