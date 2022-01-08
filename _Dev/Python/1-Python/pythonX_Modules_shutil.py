
"""
https://www.geeksforgeeks.org/python-shutil-copy2-method/

Shutil module in Python provides many functions of high-level operations on files and collections of files. 
It comes under Python’s standard utility modules. This module helps in automating process of copying and removal 
of files and directories.

shutil.copy2() method in Python is used to copy the content of source file to destination file or directory. 
This method is identical to shutil.copy() method but it also try to preserves the file’s metadata.

Source must represent a file but destination can be a file or a directory. If the destination is a directory 
then the file will be copied into destination using the base filename from source. Also, destination must be 
writable. If destination is a file and already exists then it will be replaced with the source file otherwise 
a new file will be created.

Syntax: shutil.copy2(source, destination, *, follow_symlinks = True)
Parameter: 
source: A string representing the path of the source file. 
destination: A string representing the path of the destination file or directory. 
follow_symlinks (optional) : The default value of this parameter is True. If it is False and source 
represents a symbolic link then it attempts to copy all metadata from the source symbolic link to the 
newly-created destination symbolic link. This functionality is platform dependent.
Note: The ‘*’ in parameter list indicates that all following parameters (Here in our case ‘follow_symlinks’) 
are keyword-only parameters and they can be provided using their name, not as positional parameter.
Return Type: This method returns a string which represents the path of newly created file. 
"""

###############################################################################################
# Code #1: Use of shutil.copy2() method to copy file from source to destination 
###############################################################################################

import os
import shutil

# path
path = '/home/User/Documents'

# List files and directories
# in '/home/User/Documents'
print("Before copying file:")
print(os.listdir(path))


# Source path
source = "/home/User/Documents/file.txt"

# Print the metadeta
# of source file
metadata = os.stat(source)
print("Metadata:", metadata, "\n")

# Destination path
destination = "/home/User/Documents/file(copy).txt"

# Copy the content of
# source to destination
dest = shutil.copy2(source, destination)

# List files and directories
# in "/home / User / Documents"
print("After copying file:")
print(os.listdir(path))

# Print the metadata
# of the destination file
matadata = os.stat(destination)
print("Metadata:", metadata)

# Print path of newly
# created file
print("Destination path:", dest)



###############################################################################################
# Code #2: If destination is a directory 
###############################################################################################

import os
import shutil

# path
path = '/home/User/Documents'

# List files and directories
# in '/home/User/Documents'
print("Before copying file:")
print(os.listdir(path))


# Source path
source = "/home/User/Documents/file.txt"

# Print the metadeta
# of source file
metadata = os.stat(source)
print("Metadata:", metadata, "\n")

# Destination path
destination = "/home/User/Documents/file(copy).txt"

# Copy the content of
# source to destination
dest = shutil.copy2(source, destination)

# List files and directories
# in "/home / User / Documents"
print("After copying file:")
print(os.listdir(path))

# Print the metadata
# of the destination file
matadata = os.stat(destination)
print("Metadata:", metadata)

# Print path of newly
# created file
print("Destination path:", dest)


###############################################################################################
# Code #3: Possible errors while using shutil.copy2() method 
###############################################################################################

import shutil

# If the source and destination
# represents the same file
# 'SameFileError' exception
# will be raised

# If the destination is
# not writable
# 'PermissionError' exception
# will be raised

# Source path
source = "/home/User/Documents/file.txt"

# Destination path
destination = "/home/User/Documents/file.txt"

# Copy the content of source to destination
try:
    shutil.copy2(source, destination)
    print("File copied successfully.")
# If source and destination are same
except shutil.SameFileError:
    print("Source and destination represents the same file.")
# If there is any permission issue
except PermissionError:
    print("Permission denied.")
# For other errors
except:
    print("Error occurred while copying file.")

