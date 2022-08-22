
import os
import json

os.system("clear") # Linux - OSX
#os.system("cls") # Windows

# Get Environmental Variable
#os.environ["python3"]           # raises KeyError if not present
os.getenv("python3")            # defaults to None if not present
os.getenv("python3", "default") # defaults to default value if not present

# Get All Environmental Variables as dict
json.dumps(dict(**os.environ))

# List files and directories
path = '.'
print(os.listdir(path))

# Current working dir
print(os.getcwd())
print(os.path.dirname(__file__))

# Print the metadeta
# of source file
metadata = os.stat("/Users/hukanege/Google Drive/VSCode/aws-templates/_Dev/Python/1-Python/pythonX_Modules_os.py")
print("Metadata:", metadata, "\n")

print(os.path.relpath)