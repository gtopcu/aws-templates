
import os, sys, sysconfig, shutil, subprocess
from pathlib import Path # PurePath, PosixPath, WindowsPath
import glob

# subprocess.run(["python", "app.py", "--docs_dir", "/docs")
# subprocess.check_call([
#     "pip",
#     "install",
#     "-r", "lambda/requirements.txt",
#     "-t", "build/lambda_package"
# ])

# Setup the environment
# !pip install -q -U immutabledict sentencepiece 

# import psutil
# psutil.virtual_memory()

def get_env(env_name: str, default:str | None) -> str | None:
    return os.getenv(env_name, str)    
    # os.environ.get(env_name, default)

def main():
    
    print("------------------------------ main ------------------------------")

    # python3 -m sysconfig
    # sysconfig.get_python_version()  # 3.13 
    # sysconfig.get_platform()        # macosx-10.13-universal
    
    # sys.path[0]
    # sys.version          # 3.11.5 (v3.11.5:cce6ba91b3, Aug 24 2023, 10:50:31) [Clang 13.0.0 (clang-1300.0.29.30)]
    # sys.version_info     # sys.version_info(major=3, minor=11, micro=5, releaselevel='final', serial=0)
    # sys.platform         # darwin
    # sys.argv
    # sys.stdout
    # sys.stdin
    # sys.stderr
    # sys.maxsize
    # sys.path
    # sys.modules
    # sys.gettrace()
    # sys.settrace()
    # sys.executable
    # sys.exc_info()
    # sys.exc_type
    # sys.exc_value
    # sys.exc_traceback
    # sys.last_type
    # sys.exit(0)
    # exit(1)

    # for dirname, dirpath, filename in os.walk('.'): # /dir
    #     for filename in filename:
    #         print(os.path.join(dirname, filename))

    # https://docs.python.org/3/library/os.html
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

    # https://docs.python.org/3/library/shutil.html#module-shutil 
    # High-level file and directory handling
    # To preserve all file metadata from the original, use copy2() instead.
    # shutil.copy(src, dst, *, follow_symlinks=True)        # Copies the file src to the file or directory dst
    # shutil.copyfileobj(fsrc, fdst[, length])              #  
    # shutil.copyfile(src, dst, *, follow_symlinks=True)    # no metadata
    # shutil.copymode()
    # shutil.chown("path", "user", "group")   
    # shutil.copytree(src, dst) # symlinks=False, ignore=None, copy_function=copy2, ignore_dangling_symlinks=False, dirs_exist_ok=False)
    # shutil.rmtree("os/makedirs")
    # shutil.move("/source", "target")      # same as mv
    # shutil.ignore_patterns(*patterns)     # used in copytree()
    # shutil.disk_usage(path)
    # ------------------------------------------------------------------------------------------
    # https://docs.python.org/3/library/shutil.html#shutil.unpack_archive
    # shutil.make_archive("build/lambda", "zip", "build/lambda_package") # zip/tar
    # shutil.get_archive_formats()
    # shutil.unpack_archive(filename[, extract_dir[, format[, filter]]])
    # ------------------------------------------------------------------------------------------
    # archive_name = os.path.expanduser(os.path.join('~', 'myarchive'))
    # root_dir = os.path.expanduser(os.path.join('~', '.ssh'))
    # make_archive(archive_name, 'gztar', root_dir)
    # ------------------------------------------------------------------------------------------
    # from shutil import make_archive
    # archive_name = os.path.expanduser(os.path.join('~', 'myarchive'))
    # make_archive(archive_name, 'tar', root_dir='tmp/root', base_dir='structure/content')
    # ------------------------------------------------------------------------------------------

    # path = Path()                     # .
    # path = Path.home()                # /Users/gtopcu
    # path = Path(__file__)             # /Users/gtopcu/.../utils/utils.py - doesnt work in .ipynb
    # path = Path('file:///usr/bin')
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

    # ------------------------------------------------------------------------------------------

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
