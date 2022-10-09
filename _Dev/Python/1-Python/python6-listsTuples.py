

########################################################################################
# Lists & Tuples(immutable & faster)
########################################################################################

records = ["1", "2", "3"] 
popItem = records.pop() 
print(popItem)
print("3" not in records)

records.append(["embeddedList1", "embeddedList2"])
records.extend(["4", "5"])
for record in records:
    print(record)

cities = ["Vienna", "London", "Paris", "Berlin", "Zurich", "Hamburg"]
print(cities[0:3])

cities.remove("London")
print(cities)
print(cities.index("Zurich"))

cities.insert(0, "Istanbul")
print(cities)

t = ("tuples", "are", "immutable")
print(t[0])

myTuple = (1, 2, 3)
print(myTuple.count(0))
print(myTuple.index(3))
print(myTuple[2])

# 2-tuple list
myListWithTwoTuples = [('house', 'Haus'), ('cat', ''), ('red', 'rot')]
print(myListWithTwoTuples)

# COPY - List references exactly the same objects, nested lists tuples dicts etc
person1 = ["Mike", ["5th Avenue", "NYC"]]
person2 = person1.copy()
person2[0] = "Sarah"
person2[1][0] = "6th Avenue"
print(person2)
print(person1)

# DEEP COPY - Creates new lists tuples dicts. Strings reference the same objects
from copy import deepcopy
person1 = ["Mike", ["5th Avenue", "NYC"]]
person2 = deepcopy(person1)
person2[0] = "Sarah"
person2[1][0] = "6th Avenue"
print(person2)
print(person1)


########################################################################################
# Loops
########################################################################################

count = 2
while count > 0:
    print("counting..")
    count = count-1

n = 10
for i in range(n, 3):
    print(i)

