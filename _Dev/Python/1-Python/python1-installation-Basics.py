#
# Python Cheatsheet - GT
# https://python-course.eu/python-tutorial/

# Install
# https://www.python.org/downloads/
# #!/usr/bin/env python3 (linux) 
# #!/usr/bin python3 (mac)
# #!/usr/bin/python3 (dir)

# PIP
# https://packaging.python.org/en/latest/tutorials/installing-packages/
# curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
# sudo python3 get-pip.py
# quit()
# sudo python3 -m pip install --upgrade pip
# python3 -m pip install --upgrade pip setuptools wheel

# pip3 install <package>
# python3 -m pip install "SomeProject==1.4"
# python3 -m pip install --user SomeProject
# python3 -m pip install --index-url http://my.package.repo/simple/ SomeProject
# pip install -r requirements.txt -t lib
# pip install --upgrade -r requirements.txt
# pip install -t $PWD pymysql
# pip uninstall <package>
# pip list
# pip freeze

# virtualenv/venv
# https://packaging.python.org/en/latest/tutorials/installing-packages/#creating-virtual-environments
# python3 -m venv .venv
# source .venv/bin/activate
# python3 -m pip install --upgrade virtualenv
# python -m pip install -e . (creates a virtual env)


# piptools
# https://pypi.org/project/pip-tools/
# pip install pip-tools
# pip-compile requirements/base-requirements.in
# pip-compile requirements/dev-requirements.in
# pip-compile --upgrade-package requests==2.0.0

# Install Jupyter
# pip3 install -U jupyter

# *********************************************************************************************************
# SHELL
# *********************************************************************************************************
# 
# python3
# python3 myProgram.py
# python3 + TAB: shows installed modules
# exit() or Ctrl-D (i.e. EOF) to exit

# Run module:
# python -m unittest

# Environment:
# PYTHONPATH

# Linting
# https://github.com/marketplace/actions/pylinter

# Terminal: "Hello World"
print("Hello World")
print(1, "b", sep=":", end="\n")

# output into sys.stderr & sys.stdout:
import sys
print("Error output", file=sys.stderr)
print("Standard output", file=sys.stdout)

# Input
color = input("Which colour?\n")
print(color)

myInt = int(input("Gimme an integer please"))
print(myInt)

age = eval(input("Age?:"))
print(age)


# 4.567 * 8.323 * 17 -> _
# The most recent output value is automatically stored by the interpreter in a special variable with 
# the name "_". So we can print the output from the recent example again by typing an underscore 
# after the prompt. The underscore can be used in other expressions like any other variable.
# The underscore variable is only available in the Python shell. It's NOT available in Python scripts/programs.

# *********************************************************************************************************
# Variables
# *********************************************************************************************************

maximal = 124
width = 94
print(maximal - width)

# Multiline statements
l = ["A", 42, 78, "Just a String"]
for char in l:
     print(char)
