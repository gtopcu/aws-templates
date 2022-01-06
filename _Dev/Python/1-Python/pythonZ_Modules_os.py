
import os

os.system("clear") # Linux - OSX
#os.system("cls") # Windows

# List files and directories
path = '.'
print(os.listdir(path))

# Print the metadeta
# of source file
metadata = os.stat("./python26-os.py")
print("Metadata:", metadata, "\n")

