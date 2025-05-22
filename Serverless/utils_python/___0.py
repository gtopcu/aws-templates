

import os
from pathlib import Path

import glob

# for dirpath, dirnames, filenames in os.walk('.'):
#     for filename in filename:
#         counter = 0
#         # print(os.path.join(dirname, filename))
#         if filename.endswith(".py"):
#             with open(os.path.join(dirname, filename), "r") as file:
#                 text = file.read()
#                 print(filename, len(text))

path = Path(__file__)
# print(path)

# path.glob("*.py")
# path.rglob("*.py")

# data:bytes = path.read_bytes()
# text: str = data.decode("utf-8", errors="replace")
# text = path.read_text("utf-8", errors="replace", newline="\n")

# from io import TextIOWrapper
# with path.open(mode="r", buffering=-1, encoding="utf-8", errors="replace", newline="\n") as file:
#     print(file.read(-1))

# for dirpath, dirnames, filenames in path.parent.walk():
#     print(dirpath, dirnames, filenames)

print(os.listdir())
