
import os, sys, shutil
from pathlib import Path # PurePath, PosixPath, WindowsPath
import glob

def get_env(env_name: str, default:str | None) -> str | None:
    return os.getenv(env_name, str)    
    # os.environ.get(env_name, default)

def main():
    
    print("------------------------------ main ------------------------------")

    # os.system("clear")
    # os.getenv("ENV", "default")
    # os.putenv("ENV", "value")
    # os.environ.get(env_name, default)
    
    # print(__file__)
    # os.getcwd())
    # os.listdir('.')
    # os.curdir     # .
    # os.pardir     # ..
    # os.mkdir("/dir")
    # os.makedirs("os/makedirs", exist_ok=False) # FileExistsError:
    # os.rmdir("dir")
    # os.remove("file")
    # os.rename("file1", "file2"))
    # os.chown("path", userID, groupID, follow_symlinks=False)
    # os.chmod("file", intMode)

    # os.path.join(current_path, filename)
    # os.path.isdir(path)
    # os.path.isfile(path)
    # os.path.islink(path)          
    # os.path.exists(path)
    # os.path.getsize(path)
    # os.path.basename(path)
    # os.path.dirname(__file__)
    # os.path.abspath(__file__)     # /Users/gtopcu/.../utils/utils.py
    # os.path.realpath(__file__)    # /Users/gtopcu/.../utils/utils.py
    # os.path.expanduser('~')       # Path.home()

    # shutil.rmtree("os/makedirs")
    # shutil.chown("path", "user", "group")   
    # shutil.move("/source", "target")      # same as mv

    # path = Path()                     # .
    # path = Path.home()                # /Users/gtopcu
    # path = Path(__file__)             # /Users/gtopcu/.../utils/utils.py - doesnt work in .ipynb
    # path.__str__()
    # print(path.parent)                # /Users/gtopcu/.../utils
    # print(path.parts)                 # ('/', 'Users', 'gtopcu', ...., 'utils', 'utils.py')
    # path            # /Users/gtopcu
    # path.name       # gtopcu
    # path.stem       # gtopcu - filename without extension
    # path.suffix     # .py
    # path.drive      # empty
    # path.root       # /
    # path.anchor     # /

    # Path.cwd()        # /Users/gtopcu/My Drive/VSCode
    # Path.absolute()
    # Path.resolve(strict=False)
    # Path.joinpath("Desktop").mkdir(exist_ok=True)
    # with path.open() as f:
    #     return json.load(f)
    # Path.parent()
    # Path.parents[0]   # Nth parent
    # Path.chmod(path, intMode, follow_symlinks=True)
    # Path.group()
    # Path.exists()
    # Path.is_file()
    # Path.is_dir()
    # Path.is_symlink()
    # Path.iterdir()
    # Path.as_uri(path)                 # file:///Users/gtopcu/.../utils.py
    # Path.mkdir(Path, mode = 511, parents = False, exist_ok = False)
    # Path.rmdir() # must be empty
    # Path.unlink(missing_ok=True)
    # Path.touch(Path, mode = 438, exist_ok = True)
    # Path.owner(Path)
    # Path.match("pattern")
    # Path.glob(Path, pattern="*")
    # Path.rglob(Path, pattern="*")

    # print(glob.glob("?????.py")
    # print(glob.glob("*.py"))
    # print(glob.glob("*.*"))
    # print(glob.glob("[abc]*.py")) #[] first char should be a or
    # print(glob.glob("[!abc]*.py")) #[] first char should NOT be a or b
    # globs = glob.iglob("**/utils_*.py", root_dir="/Users/gtopcu/", recursive=True, include_hidden=True)
    # print(globs.__next__())
    # for i, cglob in enumerate(globs, 1):
    #     print(i, cglob, sep=":")



if __name__ == "__main__":
    main()
