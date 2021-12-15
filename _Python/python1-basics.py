#
# Python Cheatsheet - GT
# https://python-course.eu/python-tutorial/

# Install
# https://www.python.org/downloads/
# curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
# python3 get-pip.py
# quit()
#
# Install Jupyter
# pip install -U jupyter
# 
# *********************************************************************************************************
# SHELL
# *********************************************************************************************************
# 
# python3
# python3 myProgram.py
# python3 + TAB: shows installed modules
# exit() or Ctrl-D (i.e. EOF) to exit

# Terminal: "Hello World"
print("Hello World")

# Input
# color = input("Which colour?\n")
# print(color)

# 4.567 * 8.323 * 17 -> _
# The most recent output value is automatically stored by the interpreter in a special variable with 
# the name "_". So we can print the output from the recent example again by typing an underscore 
# after the prompt. The underscore can be used in other expressions like any other variable.
# The underscore variable is only available in the Python shell. It's NOT available in Python scripts/programs.

# *********************************************************************************************************
# Variables
# *********************************************************************************************************
# It's simple to use variables in the Python shell. If you are an absolute beginner and if you don't 
# know anything about variables, please refer to our chapter about variables and data types. 
# Values can be saved in variables. Variable names don't require any special tagging, like they do in Perl, 
# where you have to use dollar signs, percentage signs and at signs to tag variables:
maximal = 124
width = 94
print(maximal - width)

# Multiline statements
l = ["A", 42, 78, "Just a String"]
for char in l:
     print(char)

# *********************************************************************************************************
# Strings
# *********************************************************************************************************
# Strings are created by putting a sequence of characters in quotes. Strings can be surrounded by 
# single quotes, double quotes or triple quotes, which are made up of three single or three double quotes. 
# Strings are immutable. In other words, once defined, they cannot be changed. 
print("Hello" + " " + "World")

# A string in triple quotes can span several lines without using the escape character:
# city = """
# ... Toronto is the largest city in Canada 
# ... and the provincial capital of Ontario. 
# ... It is located in Southern Ontario on the 
# ... northwestern shore of Lake Ontario.
# ... """
# print(city)

# Multiplication on strings is defined, which is essentially a multiple concatenation:
# ".-." * 4
# OUTPUT:
# '.-..-..-..-.'


# *********************************************************************************************************
# Runnable scripts under Linux
# *********************************************************************************************************

# A Python script can also be started like any other script under Linux, e.g. Bash scripts. Two steps are 
# necessary for this purpose: the shebang line #!/usr/bin/env python3 has to be added as the first line 
# of your Python code file. Alternatively, this line can be #!/usr/bin/python3, if this is the location 
# of your Python interpreter. Instead using env as in the first shebang line, the interpreter is searched 
# for and located at the time the script is run. This makes the script more portable. 
# Yet, it also suffers from the same problem: The path to env may also be different on a per-machine basis. 
# The file has to be made executable: The command "chmod +x scriptname" has to be executed on a Linux shell, 
# e.g. bash. "chmod 755 scriptname" can also be used to make your file executable. In our example:
# $ chmod +x my_first_simple_program.py

# We illustrate this in a bash session:
# bernd@marvin:~$ more my_first_simple_script.py 
# !/usr/bin/env python3
# print("My first simple Python script!")
# bernd@marvin:~$ ls -ltr my_first_simple_script.py 
# -rw-r--r-- 1 bernd bernd 63 Nov  4 21:17 my_first_simple_script.py
# bernd@marvin:~$ chmod +x my_first_simple_script.py 
# bernd@marvin:~$ ls -ltr my_first_simple_script.py 
# -rwxr-xr-x 1 bernd bernd 63 Nov  4 21:17 my_first_simple_script.py
# bernd@marvin:~$ ./my_first_simple_script.py 
# My first simple Python script!

