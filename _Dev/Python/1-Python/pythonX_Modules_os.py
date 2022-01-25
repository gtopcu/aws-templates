
import os

os.system("clear") # Linux - OSX
#os.system("cls") # Windows

# Get Environmental Variable
print(os.getenv("python3"))

# Get All Environmental Variables as dict
print(os.environ)

# List files and directories
path = '.'
print(os.listdir(path))

# Print the metadeta
# of source file
metadata = os.stat("python26-os.py")
print("Metadata:", metadata, "\n")

