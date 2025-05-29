
# logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
# traceback.print_exception(type(err), err, err.__traceback__)

# from pprint import pprint
# bowie = dict(name="David Bowie", age=86)
# pprint(bowie, indent=4, sort_dicts=False)

# os.getenv("PYTHONPATH")
# for path in sys.path:
#     print("Path: " + path)
# sys.path.append(os.getcwd() + "/.venv/lib/python3.13/site-packages")
# sys.path.insert(0, str(Path(__file__).parent))
# os.path.join(__file__, "test.txt")

# Add the parent directory to sys.path
# current_dir = os.path.dirname(os.path.abspath(__file__))
# parent_dir = os.path.dirname(os.path.dirname(current_dir))
# sys.path.append(parent_dir)

# from pathlib import Path
# Path(__file__).resolve().parent.is_dir()
# Path(__file__).absolute().joinpath("..").mkdir(mode=0o777, parents=True, exist_ok=True)
# print(Path.home())
# print(Path.cwd())

# from datetime import datetime, timezone, timedelta
# import time
# datetime.now(timezone.utc).isoformat(timespec="seconds")
# my_date + timedelta(hours=1)
# time.time()
# time.sleep(2)
# time.strftime("%Y-%m-%d %H:%M:%S")
# time.perf_counter()
# datetime.now().strftime("%Y-%m-%d %H:%M:%S")
# time.strptime("2024-03-24", "%Y-%m-%d")
# date = datetime.strptime("2024-03-24", "%Y-%m-%d").date()
# date.today()
# date.day
# date.month
# date.year
# date = datetime.strptime("2024-03-24", "%Y-%m-%d").date()
# birthday = datetime.strptime("2020-07-24", "%Y-%m-%d").date()
# age = (date.today() - birthday).days // 365
# print(age)

# os.getenv("DDB_TABLE", "table1")
# os.environ.get("DDB_TABLE", "table1")
# POSTGRE_IP = os.environ["POSTGRE_IP"]
# POSTGRE_PORT: int = os.environ.setdefault("POSTGRE_PORT", 5432)

# current_dir = os.path.dirname(os.path.abspath(__file__))
# file_path = os.path.join(current_dir, filename)
# if not os.path.exists(file_path):
#     raise FileNotFoundError(f"File not found: {file_path}")
# os.path.split(os.path.abspath(__file__))[0]
# os.path.splitext("note.txt") -> txt
# os.path.basename(__file__)
# os.path.expanduser(os.path.join("~", "myarchive"))
# os.getcwd()
# os.listdir()
# os.makedirs("test", exist_ok=True)
# os.rmdir("test")
# os.chmod("test.txt", 0o777)
# os.chown(("test.txt", 1000, 1000)
# os.system("clear")
# print(__name__)
# print(__file__)

# shutil.copytree("lambda", "build/lambda_package")
# shutil.make_archive("build/lambda", "zip", "build/lambda_package") # zip/tar
# shutil.rmtree("build/lambda_package")
# subprocess.run(["python", "app.py", "--docs_dir", "/docs")
# subprocess.check_call([
#     "pip",
#     "install",
#     "-r", "lambda/requirements.txt",
#     "-t", "build/lambda_package"
# ])


# exit(1)
# sys.exit(0)

# name: str = "John"
# name.join("Doe")
# print("PK_%s" % ID)
# "request: {}"".format(json.dumps(event))
# " ".removeprefix("")
# " ".removesuffix("")
# ",".join(mylist)
# " ".casefold()
# " ".strip()
# "str".isdigit()
# "str".isalnum()
# "mr. gokhan topcu".title()
# any(char in string.digits for char in pw)


# try:
#     print(1/0)
# except ZeroDivisionError as e:
#     print(f"Error during operation: {str(e)}")



