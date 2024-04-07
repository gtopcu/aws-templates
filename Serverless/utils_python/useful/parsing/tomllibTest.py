

# https://www.youtube.com/watch?v=D_Jb52jw2HY

import tomllib # Python 3.11
from pprint import pprint
import os

def load_toml(filename) -> dict:
    """ Loads TOML data from file and returns as a dict """
    with open(filename, "rb") as f:
        tomldata:dict =  tomllib.load(f)
        return tomldata

def main():
    tomldata:dict = load_toml("tomllib.toml")
    pprint(tomldata, sort_dicts=False)
    print(tomldata)
    print("done")

if __name__ == "__main__":
    main()