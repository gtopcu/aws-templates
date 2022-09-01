
# https://www.tutorialsteacher.com/python/collections-module

import collections

# The namedtuple() function returns a tuple-like object with named fields. 
# These field attributes are accessible by lookup as well as by index.
student = collections.namedtuple('student', [name, age, marks])
s1 = student("Imran", 21, 98)
print(s1.name)
print(s1[0])


# The OrderedDict() function is similar to a normal dictionary object in Python. 
# However, it remembers the order of the keys in which they were first inserted.
d1 = collections.OrderedDict()
d1['A'] = 65
d1['C'] = 67
d1['B'] = 66
d1['D'] = 68

for k,v in d1.items():
    print (k,v)

# A deque object support appends and pops from either ends of a list. It is more memory 
# efficient than a normal list object. In a normal list object, the removal of any item causes 
# all items to the right to be shifted towards left by one index. Hence, it is very slow.
q=collections.deque([10,20,30,40])
q.appendleft(0)
# deque([0, 10, 20, 30, 40])
q.append(50)
# deque([0, 10, 20, 30, 40, 50])
q.pop()
# 50
# deque([0, 10, 20, 30, 40])
q.popleft()
# 0
# deque([10, 20, 30, 40])