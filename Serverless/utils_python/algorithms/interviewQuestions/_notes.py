
# export PATH=$PATH:/usr/local/go/bin
# git branch -l remove checkout switch
# chmod u+rwx keypair.pem
# chmod 400
# ssh -i keypair.pem ec2-user@192.168.1.1
# .aws /etc/hosts, var/log

# --------------------------------------------------------------------------------------------

# import os
# os.environ['AWS_ACCESS_KEY_ID'] = '...'
# os.getenv('AWS_SECRET_ACCESS_KEY', 'default')

# BaseException ->     
#   Exception -> SystemExit     
#   StandardError -> ValueError: int("A"), KeyError: dict['key1'], TypeError: str[0]='a',     
#   IndexError, AttributeError, NameError, AssertionError, StopIteration, ArithmeticError,     
#   ZeroDivisionError, NotImplementedError, RuntimeError, SystemError

# reversed/sorted (generator), round, abs, min-max, sum, power, enumerate, zip, filter, reduce, chr/ord, 
# callable, any/all, iter, isinstance, id, type, join, slice, issubclass, [*filter()]

# sys.version
# sys.executable
# os.path.dirname(__file__)
# os.path.join(os.path.dirname(os.path.abspath(__file__)), 'test.txt')
# for dirname, dirpath, filename in os.walk('.'): # /dir
# output = 'username_%s' % name
# def mandatoryKwargs(self, *, name: str, age: int): ...
# credentials = boto3.session.Session().get_credentials()
# class MyClass[T: (int, float)]:

# object.super()._new_()

# def __eq__(self, other: Self) -> bool:    
#   return self.name == other.name and self.age == other.age    self.__dict__ == other.__dict__
# def __repr__(self) -> str:         r
#   return f"SampleClass(name={self.name}, age={self.age})"
# @property 
# def total(self):     
#   return self.item_price * self.item_count

# mylist = [*range(3)]
# mylist = list(map(lambda x: x*x, mylist))
# map(lambda x: (x, x * 2))
# flipped = nums_rdd.map(lambda x: (x[1], x[0]))
# list = sorted(dict, key=dict.get, reverse=True)
# list = sorted(occurrences, key=lambda x:occurrences[x], reverse=True)

# r: slice = slice(None, None, -1)
# print(my_list[r])

# set() tuple(1, ) tuple((1,2))
# mytuple = tuple((1, 2))
# x, y = mytuple # unpacking
# tuple3 = tuple1 + tuple2
# mylist.pop(1) -> Any: IndexError# mydict.popitem() -> Any# mydict.pop("key1") -> Any: KeyError# myset.pop() -> Any# myset.remove(element) -> None: KeyError# myset.discard(element) -> None: No error
# iterator = (x for x in range(6))print(next(iterator))for i in iterator:        print(i)
# mylist1 = [1,2,3]
# mylist2 = [4,5,6]
# print(dict(zip(mylist1, mylist2)))
# mydict = { x:y for x,y in zip(mylist1, mylist2) }
# print(mydict)
# datetime.replace(hour=0)
# datetime.timedelta(day=1)
# bytes = random.randbytes(10) # 0-255
# functools reduce, cache, lru_cache
# from collections import deque, OrderedDict(move to left)
# heapq._heapify_max()
# from . import database as db
# import .database
# python -m project.app
# pip list | grep pandas

# --------------------------------------------------------------------------------------------
# Pandas
# --------------------------------------------------------------------------------------------
# statistics.median(self.items)
# random.rand(1,2) / zeros/ones/ arange(0, 10, 2)
# df = pd.read_csv()
# df
# df.shape
# df.values
# df.head(3)
# df.describe()
# df.plot()
# X = df.drop(columns=["genre"]) #does not modify original
# y = df["genre"]

