

# my_set = {0, 1, 2} # set()
# if 0 in my_set | if 0 not in my_set 
# my_set.add(1)
# my_set.remove(1)
# my_set.discard(1)
# my_set.pop()
# my_set.update()
# my_set.union()
# my_set.copy()
# my_set.clear()
# my_set.issubset()
# my_set.issuperset()
# my_set.isdisjoint()
# my_set.difference()
# my_set.difference_update()
# my_set.intersection()
# my_set.intersection_update()
# my_set.symmetric_difference()
# my_set.symmetric_difference_update()

# my_list = [0, 1, 2]
# del my_list[0]
# my_list.append(3)
# my_list.extend([4, 5])
# my_list.insert(0, "A")
# my_list.pop()
# my_list.count(0)
# my_list.remove(0)
# my_list.copy()
# my_list.clear()
# my_list.sort(reverse=True)
# my_list.reverse()

# my_dict = {}
# del my_dict["key"]
# my_dict.get(key="key", default=None)
# my_dict.pop(key="key", default=None)
# my_dict.popitem()
# my_dict.keys()
# my_dict.values()
# my_dict.items()
# my_dict.copy()
# my_dict.clear()
# my_dict.fromkeys(my_list)
# my_dict.setdefault(key="key", default=None)
# my_dict.update(my_dict)

# import os
# from pathlib import Path

# print(os.listdir())

# for dirpath, dirnames, filenames in os.walk('.'):
#     for filename in filename:
#         counter = 0
#         # print(os.path.join(dirname, filename))
#         if filename.endswith(".py"):
#             with open(os.path.join(dirname, filename), "r") as file:
#                 text = file.read()
#                 print(filename, len(text))

# path = Path(__file__)
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

# path = Path().cwd()
# for p in path.iterdir():
#     print(p.absolute())
