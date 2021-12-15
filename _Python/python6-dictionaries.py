# https://python-course.eu/python-tutorial/dictionaries.php

# Dictionaries:     Elements can only be accessed via their keys and not via their position
#                   map-value like HashMap in Java, no duplicates for the same key (also like Set)
#                   Can grow & shrink, be included in lists & tuples and vice versa
#                   Syntax is exactly like JSON
#                   KeyError if key is not present
#                   In Python 3.7 and all later versions, sorted by the order of item insertion
#                   In case a keys is defined multiple times, the value of the last wins
#                   Only immutable types can be used as keys, no lists or dictionaries, but tuples are ok


# Defining a dictionary
city_population = {
                    "New York City": 8550405, 
                    "Los Angeles": 3971883,
                    "İstanbul": 20313682, 
                    "Ankara": 7313682, 
                }
print(city_population)

# Getting an item by key
print(city_population["New York City"])

# Adding new keys
city_population["Halifax"] = 390096
print(city_population)

# Operations
del city_population["Los Angeles"]
popped = city_population.pop("İstanbul")
(city, population) = city_population.popitem()
print(city, population)
print(city_population)
print(len(city_population))
print("new york city".upper() in city_population)
print(city_population.get("İstanbul", 0))
city_population.clear()
print(city_population)

# Defining empty dictionary and adding later
ages = {}
ages["Gökhan"] = 36
ages["Göknur"] = 31
print(ages)

# Copy - Deep Copy: Same as lists
ages2 = ages.copy()
print(ages2)
from copy import deepcopy
ages3 = deepcopy(ages)
print(ages)

# Merging
knowledge = {"Frank": {"Perl"}, "Monica":{"C","C++"}}
knowledge2 = {"Guido":{"Python"}, "Frank":{"Perl", "Python"}}
knowledge.update(knowledge2)
print(knowledge)

# Loops
for key in ages:
    print(key)
for key2 in ages.keys():
    print(key2)
for value in ages.values():
    print(value)
for key, value in ages.items():
    print(key, value)



"""

Like lists, they can be easily changed, can be shrunk and grown ad libitum at run time. 
They shrink and grow without the necessity of making copies. Dictionaries can be contained 
in lists and vice versa.

A list is an ordered sequence of objects, whereas dictionaries are unordered sets. However, 
the main difference is that items in dictionaries are accessed via keys and not via their position.

More theoretically, we can say that dictionaries are the Python implementation of an abstract data type, 
known in computer science as an associative array. 

Associative arrays consist - like dictionaries of (key, value) pairs, such that each possible key appears 
at most once in the collection. Any key of the dictionary is associated (or mapped) to a value. 
The values of a dictionary can be any type of Python data. So, dictionaries are unordered key-value-pairs. 

Dictionaries are implemented as hash tables, and that is the reason why they are known as "Hashes" 
in the programming language Perl.

Dictionaries don't support the sequence operation of the sequence data types like strings, tuples and lists. 
Dictionaries belong to the built-in mapping type, but so far, they are the sole representative of this kind!

At the end of this chapter, we will demonstrate how a dictionary can be turned into one list, 
containing (key,value)-tuples or two lists, i.e. one with the keys and one with the values. 
This transformation can be done reversely as well.

Examples of Dictionaries
Our first example is a dictionary with cities located in the US and Canada and their corresponding population. 
We have taken those numbers out the "List of North American cities by population" from Wikipedia 
(List of North American cities by population)

If we want to get the population of one of those cities, all we have to do is to use the name of the city 
as an index. We can see that dictonaries are enclosed in curly brackets. 
They contain key value pairs. A key and its corresponding value are separated by a colon:

city_population = {"New York City": 8_550_405, 
                   "Los Angeles": 3_971_883, 
                   "Toronto": 2_731_571, 
                   "Chicago": 2_720_546, 
                   "Houston": 2_296_224, 
                   "Montreal": 1_704_694, 
                   "Calgary": 1_239_220, 
                   "Vancouver": 631_486, 
                   "Boston": 667_137}
print(city_population)

OUTPUT:
8550405
We can access the value for a specific key by putting this key in brackets following the name of the dictionary:

city_population["New York City"]
OUTPUT:
8550405
city_population["Toronto"]
OUTPUT:
2731571
city_population["Boston"]
OUTPUT:
667137
What happens, if we try to access a key, i.e. a city in our example, which is not contained in the dictionary? 
We raise a KeyError:

city_population["Detroit"]
OUTPUT:
---------------------------------------------------------------------------
KeyError                                  Traceback (most recent call last)
<ipython-input-5-80e422418d76> in <module>
----> 1 city_population["Detroit"]
KeyError: 'Detroit'

A frequently asked question is if dictionary objects are ordered. The uncertainty arises from the fact 
that dictionaries were not sorted in versions before Python 3.7. In Python 3.7 and all later versions, 
dictionaries are sorted by the order of item insertion. In our example this means the dictionary 
keeps the order in which we defined the dictionary. You can see this by printing the dictionary:

city_population
OUTPUT:
{'New York City': 8550405,
 'Los Angeles': 3971883,
 'Toronto': 2731571,
 'Chicago': 2720546,
 'Houston': 2296224,
 'Montreal': 1704694,
 'Calgary': 1239220,
 'Vancouver': 631486,
 'Boston': 667137}

Yet, ordering doesn't mean that you have a way of directly calling the nth element of a dictionary. 
So trying to access a dictionary with a number - like we do with lists - will result in an exception:

city_population[0]
OUTPUT:
---------------------------------------------------------------------------
KeyError                                  Traceback (most recent call last)
<ipython-input-7-a4816f909f86> in <module>
----> 1 city_population[0]
KeyError: 0

It is very easy to add another entry to an existing dictionary:

city_population["Halifax"] = 390096
city_population
OUTPUT:
{'New York City': 8550405,
 'Los Angeles': 3971883,
 'Toronto': 2731571,
 'Chicago': 2720546,
 'Houston': 2296224,
 'Montreal': 1704694,
 'Calgary': 1239220,
 'Vancouver': 631486,
 'Boston': 667137,
 'Halifax': 390096}

So, it's possible to create a dictionary incrementally by starting with an empty dictionary. 

We haven't mentioned so far, how to define an empty one. It can be done by using an empty pair of brackets. 
The following defines an empty dictionary called city:

city_population = {}
city_population
city_population['New York City'] = 8550405
city_population['Los Angeles'] = 3971883
city_population

Looking at our first examples with the cities and their population, you might have gotten the wrong 
impression that the values in the dictionaries have to be different. The values can be the same, 
as you can see in the following example. In honour to the patron saint of Python "Monty Python", 
we'll have now some special food dictionaries. What's Python without "bacon", "egg" and "spam"?

food = {"bacon": "yes", "egg": "yes", "spam": "no" }
food

Keys of a dictionary are unique. In casse a keys is defined multiple times, the value of the last "wins":

food = {"bacon" : "yes", "spam" : "yes", "egg" : "yes", "spam" : "no" }
food

Our next example is a simple English-German dictionary:

en_de = {"red" : "rot", "green" : "grün", "blue" : "blau", "yellow":"gelb"}
print(en_de)
print(en_de["red"])

What about having another language dictionary, let's say German-French?
Now it's even possible to translate from English to French, even though we don't have an 
English-French-dictionary. de_fr[en_de["red"]] gives us the French word for "red", i.e. "rouge":

de_fr = {"rot": "rouge", "grün": "vert", "blau": "bleu", "gelb": "jaune"}
en_de = {"red": "rot", "green": "grün", "blue": "blau", "yellow": "gelb"}
print(en_de)
print(en_de["red"])
de_fr = {"rot" : "rouge", "grün" : "vert", "blau" : "bleu", "gelb":"jaune"}
print("The French word for red is: " + de_fr[en_de["red"]])

We can use arbitrary types as values in a dictionary, but there is a restriction for the keys. 
Only immutable data types can be used as keys, i.e. no lists or dictionaries, but tuples can 
If you use a mutable data type as a key, you get an error message:

dic = {[1,2,3]: "abc"}
Tuple as keys are okay, as you can see in the following example:

dic = {(1, 2, 3): "abc", 3.1415: "abc"}
dic


Let's improve our examples with the natural language dictionaries a bit. 
We create a dictionary of dictionaries:

en_de = {"red" : "rot", "green" : "grün", "blue" : "blau", "yellow":"gelb"}
de_fr = {"rot" : "rouge", "grün" : "vert", "blau" : "bleu", "gelb":"jaune"}
de_tr = {"rot": "kırmızı", "grün": "yeşil", "blau": "mavi", "gelb": "jel"}
en_es = {"red" : "rojo", "green" : "verde", "blue" : "azul", "yellow":"amarillo"}

dictionaries = {"en_de" : en_de, "de_fr" : de_fr, "de_tr": de_tr, "en_es": en_es}
dictionaries

cn_de = {"红": "rot", "绿" : "grün", "蓝" : "blau", "黄" : "gelb"}
de_ro = {'rot': 'roșu', 'gelb': 'galben', 'blau': 'albastru', 'grün': 'verde'}
de_hex = {"rot" : "#FF0000", "grün" : "#00FF00", "blau" : "0000FF", "gelb":"FFFF00"}
en_pl = {"red" : "czerwony", "green" : "zielony", 
         "blue" : "niebieski", "yellow" : "żółty"}
de_it = {"rot": "rosso", "gelb": "giallo", "blau": "blu", "grün": "verde"}

dictionaries["cn_de"] = cn_de
dictionaries["de_ro"] = de_ro
dictionaries["de_hex"] = de_hex
dictionaries["en_pl"] = en_pl
dictionaries["de_it"] = de_it
dictionaries

A dictionary of dictionaries.

dictionaries["en_de"]     # English to German dictionary
dictionaries["de_fr"]     # German to French
print(dictionaries["de_fr"]["blau"])    # equivalent to de_fr['blau']

de_fr['blau']
lang_pair = input("Which dictionary, e.g. 'de_fr', 'en_de': ")
word_to_be_translated = input("Which colour: ")
d = dictionaries[lang_pair]
if word_to_be_translated in d:
    print(word_to_be_translated + " --> " + d[word_to_be_translated])
dictionaries['de_fr'][dictionaries['en_de']['red']]
de_fr

for value in de_fr.values():
    print(value)
for key, value in de_fr.items():
    print(key, value)

fr_de = {}
fr_de['rouge'] = 'rot'
fr_de['vert'] = "grün"
fr_de = {}
for key, value in de_fr.items():
    fr_de[value] = key             # key and value are swapped
fr_de
de_cn = {}
for key, value in cn_de.items():
    de_cn[value] = key
de_cn

Operators in Dictionaries

len(d)	    returns the number of stored entries, i.e. the number of (key,value) pairs.
del d[k]	deletes the key k together with his value
k in d	    True, if a key k exists in the dictionary d
k not in d	True, if a key k doesn't exist in the dictionary d

Examples: The following dictionary contains a mapping from latin characters to morsecode.

morse = {
"A" : ".-", 
"B" : "-...", 
"C" : "-.-.", 
"D" : "-..", 
"E" : ".", 
"F" : "..-.", 
"G" : "--.", 
"H" : "....", 
"I" : "..", 
"J" : ".---", 
"K" : "-.-", 
"L" : ".-..", 
"M" : "--", 
"N" : "-.", 
"O" : "---", 
"P" : ".--.", 
"Q" : "--.-", 
"R" : ".-.", 
"S" : "...", 
"T" : "-", 
"U" : "..-", 
"V" : "...-", 
"W" : ".--", 
"X" : "-..-", 
"Y" : "-.--", 
"Z" : "--..", 
"0" : "-----", 
"1" : ".----", 
"2" : "..---", 
"3" : "...--", 
"4" : "....-", 
"5" : ".....", 
"6" : "-....", 
"7" : "--...", 
"8" : "---..", 
"9" : "----.", 
"." : ".-.-.-", 
"," : "--..--"
}

If you save this dictionary as morsecode.py, you can easily follow the following examples. 
At first you have to import this dictionary:

from morsecode import morse 
The numbers of characters contained in this dictionary can be determined by calling the len function:

len(morse)
38

The dictionary contains only upper case characters, so that "a" returns False, for example:

"a" in morse
"A" in morse
"a" not in morse
word = input("Your word: ")
for char in word.upper():
    print(char, morse[char])
word = input("Your word: ")
morse_word = ""
for char in word.upper():
    if char == " ":
        morse_word += "   "
    else:
        if char not in morse:
            continue          # continue with next char, go back to for
        morse_word += morse[char] + " "
print(morse_word)
for i in range(15):
    if i == 13:
        continue
    print(i)


pop() and popitem()
pop

Lists can be used as stacks and the operator pop() is used to take an element from the stack. 
So far, so good for lists, but does it make sense to have a pop() method for dictionaries? 
After all, a dict is not a sequence data type, i.e. there is no ordering and no indexing. 
Therefore, pop() is defined differently with dictionaries. 

Keys and values are implemented in an arbitrary order, which is not random, but depends on the implementation. 
If D is a dictionary, then D.pop(k) removes the key k with its value from the dictionary D 
and returns the corresponding value as the return value, i.e. D[k].

en_de = {"Austria":"Vienna", "Switzerland":"Bern", "Germany":"Berlin", "Netherlands":"Amsterdam"}
capitals = {"Austria":"Vienna", "Germany":"Berlin", "Netherlands":"Amsterdam"}
capital = capitals.pop("Austria")
print(capital)
If the key is not found, a KeyError is raised:

print(capitals)
{'Netherlands': 'Amsterdam', 'Germany': 'Berlin'}
capital = capitals.pop("Switzerland")

If we try to find out the capital of Switzerland in the previous example, we raise a KeyError. 
To prevent these errors, there is an elegant way. The method pop() has an optional second parameter, 
which can be used as a default value:

capital = capitals.pop("Switzerland", "Bern")
print(capital)
capital = capitals.pop("France", "Paris")
print(capital)
capital = capitals.pop("Germany", "München")
print(capital)

popitem
popitem() is a method of dict, which doesn't take any parameter and removes and returns 
an arbitrary (key, value) pair as a 2-tuple. If popitem() is applied on an empty dictionary, 
a KeyError will be raised.

capitals = {"Springfield": "Illinois", 
            "Augusta": "Maine", 
            "Boston": "Massachusetts", 
            "Lansing": "Michigan", 
            "Albany": "New York", 
            "Olympia": "Washington", 
            "Toronto": "Ontario"}
(city, state) = capitals.popitem()
(city, state)
print(capitals.popitem())
print(capitals.popitem())
print(capitals.popitem())
print(capitals.popitem())


Accessing Non-existing Keys
If you try to access a key which doesn't exist, you will get an error message:

locations = {"Toronto": "Ontario", "Vancouver": "British Columbia"}
locations["Ottawa"]

You can prevent this by using the "in" operator:

province = "Ottawa"
if province in locations: 
    print(locations[province])
else:
    print(province + " is not in locations")

Another method to access the values via the key consists in using the get() method. 
get() is not raising an error, if an index doesn't exist. 
In this case it will return None. 

It's also possible to set a default value, which will be returned, if an index doesn't exist:

proj_language = {"proj1":"Python", "proj2":"Perl", "proj3":"Java"}
proj_language["proj1"]
proj_language.get("proj2")
proj_language.get("proj4")
print(proj_language.get("proj4")) 
# setting a default value:
proj_language.get("proj4", "Python")

Important Methods
A dictionary can be copied with the method copy():

copy()
words = {'house': 'Haus', 'cat': 'Katze'}
w = words.copy()
words["cat"]="chat"
print(w)
print(words)

This copy is a shallow copy, not a deep copy. If a value is a complex data type like a list, 
for example, in-place changes in this object have effects on the copy as well:

trainings = { "course1":{"title":"Python Training Course for Beginners", 
                         "location":"Frankfurt", 
                         "trainer":"Steve G. Snake"},
              "course2":{"title":"Intermediate Python Training",
                         "location":"Berlin",
                         "trainer":"Ella M. Charming"},
              "course3":{"title":"Python Text Processing Course",
                         "location":"München",
                         "trainer":"Monica A. Snowdon"}
              }
trainings2 = trainings.copy()
trainings["course2"]["title"] = "Perl Training Course for Beginners"
print(trainings2)

If we check the output, we can see that the title of course2 has been changed not only in the dictionary 
training but in trainings2 as well.

Everything works the way you expect it, if you assign a new value, i.e. a new object, to a key:

trainings = { "course1": {"title": "Python Training Course for Beginners", 
                         "location": "Frankfurt", 
                         "trainer": "Steve G. Snake"},
              "course2": {"title": "Intermediate Python Training",
                         "location": "Berlin",
                         "trainer": "Ella M. Charming"},
              "course3": {"title": "Python Text Processing Course",
                         "location": "München",
                         "trainer": "Monica A. Snowdon"}
              }
trainings2 = trainings.copy()
trainings["course2"] = {"title": "Perl Seminar for Beginners",
                         "location": "Ulm",
                         "trainer": "James D. Morgan"}
print(trainings2["course2"])

If you want to understand the reason for this behaviour, we recommend our chapter "Shallow and Deep Copy".

clear()
The content of a dictionary can be cleared with the method clear(). The dictionary is not deleted, 
but set to an empty dictionary:
w.clear()
print(w)

Update: Merging Dictionaries
What about concatenating dictionaries, like we did with lists? There is someting similar for 
dictionaries: the update method update() merges the keys and values of one dictionary into another, 
overwriting values of the same key:

knowledge = {"Frank": {"Perl"}, "Monica":{"C","C++"}}
knowledge2 = {"Guido":{"Python"}, "Frank":{"Perl", "Python"}}
knowledge.update(knowledge2)
knowledge

Iterating over a Dictionary
No method is needed to iterate over the keys of a dictionary:

d = {"a":123, "b":34, "c":304, "d":99}
for key in d:
     print(key) 

However, it's possible to use the method keys(), we will get the same result:
for key in d.keys():
     print(key) 

The method values() is a convenient way for iterating directly over the values:
for value in d.values():
    print(value)

The above loop is logically equivalent to the following one:
for key in d:
    print(d[key])
We said logically, because the second way is less efficient!


If you are familiar with the timeit possibility of ipython, you can measure the time used for the 
two alternatives:

%%timeit  d = {"a":123, "b":34, "c":304, "d":99}
for key in d.keys():
    x = d[key]
%%timeit  d = {"a":123, "b":34, "c":304, "d":99}
for value in d.values():
    x = value


Connection between Lists and Dictionaries
Zipper on a Ball

If you have worked for a while with Python, nearly inevitably the moment will come, 
when you want or have to convert lists into dictionaries or vice versa. It wouldn't be too hard 
to write a function doing this. But Python wouldn't be Python, if it didn't provide such functionalities.

If we have a dictionary

D = {"list": "Liste", "dictionary": "Wörterbuch", "function": "Funktion"}
we could turn this into a list with two-tuples:

L = [("list", "Liste"), ("dictionary", "Wörterbuch"), ("function", "Funktion")]

The list L and the dictionary D contain the same content, i.e. the information content, or to express 
"The entropy of L and D is the same" sententiously. Of course, the information is harder to retrieve 
from the list L than from the dictionary D. To find a certain key in L, we would have to browse 
through the tuples of the list and compare the first components of the tuples with the key we are looking for. 
The dictionary search is implicitly implemented for maximum efficiency

Lists from Dictionaries
It's possible to create lists from dictionaries by using the methods items(), keys() and values()
keys() creates a list, which consists solely of the keys of the dictionary. 
values() produces a list consisting of the values. 
items() can be used to create a list consisting of 2-tuples of (key,value)-pairs:
"""

w = {"house": "Haus", "cat": "", "red": "rot"}
items_view = w.items()
items = list(items_view)
print(items)

keys_view = w.keys()
keys = list(keys_view)
print(keys)

values_view = w.values()
values = list(values_view)
print(values)

"""
If we apply the method items() to a dictionary, we don't get a list back, 
as it used to be the case in Python 2, but a so-called items view. The items view can be turned into 
a list by applying the list function. We have no information loss by turning a dictionary into an 
item view or an items list, i.e. it is possible to recreate the original dictionary from the view 
created by items(). Even though this list of 2-tuples has the same entropy, i.e. the information 
content is the same, the efficiency of both approaches is completely different. The dictionary data type 
provides highly efficient methods to access, delete and change the elements of the dictionary, 
while in the case of lists these functions have to be implemented by the programmer.

Turn Lists into Dictionaries
We want to show you, how to turn lists into dictionaries, if these lists satisfy certain conditions. 

Now we will create a dictionary, which assigns a dish, a country-specific dish, to a country.
For this purpose, we need the function zip(). The name zip was well chosen, because the two lists get combined, 
functioning like a zipper. The result is a list iterator. This means that we have to wrap a list() 
casting function around the zip call to get a list so that we can see what is going on:
"""

dishes = ["pizza", "sauerkraut", "paella", "hamburger"]
countries = ["Italy", "Germany", "Spain", "USA"]
iterator = zip(countries, dishes)
print(iterator)

country_specialities = list(iterator)
print(country_specialities) 

"""
Alternatively, you could have iteras over the zip object in a for loop. This way we are not creating a list, 
which is more efficient, if we only want to iterate over the values and don't need a list
"""

for country, dish in zip(countries, dishes):
    print(country, dish)

"""
Now our country-specific dishes are in a list form, - i.e. a list of two-tuples, where the first components 
are seen as keys and the second components as values - which can be automatically turned into a dictionary 
by casting it with dict().
"""
country_specialities_dict = dict(country_specialities)
print(country_specialities_dict)

"""
Yet, this is very inefficient, because we created a list of 2-tuples to turn this list into a dict. 
This can be done directly by applying dict to zip:
"""
dishes = ["pizza", "sauerkraut", "paella", "hamburger"]
countries = ["Italy", "Germany", "Spain", "USA"]
dict(zip(countries, dishes))

""" 
There is still one question concerning the function zip(). What happens, if one of the two argument lists 
contains more elements than the other one?

It's easy to answer: The superfluous elements, which cannot be paired, will be ignored:
"""

dishes = ["pizza", "sauerkraut", "paella", "hamburger"]
countries = ["Italy", "Germany", "Spain", "USA"," Switzerland"]
country_specialities = list(zip(countries, dishes))
country_specialities_dict = dict(country_specialities)
print(country_specialities_dict)

"""
Everything in One Step
Normally, we recommend not implementing too many steps in one programming expression, 
though it looks more impressive and the code is more compact. 

Using "talking" variable names in intermediate steps can enhance legibility. 
Though it might be alluring to create our previous dictionary just in one go:
"""

country_specialities_dict = dict(zip(["pizza", "sauerkraut", "paella", "hamburger"], 
                                     ["Italy", "Germany", "Spain", "USA"," Switzerland"]))
print(country_specialities_dict)

"""
Of course, it is more readable like this:
"""

dishes = ["pizza", "sauerkraut", "paella", "hamburger"]
countries = ["Italy", "Germany", "Spain", "USA"]
country_specialities_zip = zip(dishes,countries)
country_specialities_dict = dict(country_specialities_zip)
print(country_specialities_dict)

"""
We get the same result, as if we would have called it in one go.

Danger Lurking
Especialy for those migrating from Python 2.x to Python 3.x: zip() used to return a list, now it's returning 
an iterator. You have to keep in mind that iterators exhaust themselves, if they are used. 
You can see this in the following interactive session:
"""
l1 = ["a","b","c"]
l2 = [1,2,3]
c = zip(l1, l2)
for i in c:
    print(i)

"""
This effect can be seen by calling the list casting operator as well:
"""

l1 = ["a","b","c"]
l2 = [1,2,3]
c = zip(l1,l2)
z1 = list(c)
z2 = list(c)
print(z1)
print(z2)

"""
As an exercise, you may muse about the following script. Why do we get an empty directory by calling 
dict(country_specialities_zip)?
"""

dishes = ["pizza", "sauerkraut", "paella", "hamburger"]
countries = ["Italy", "Germany", "Spain", "USA"]
country_specialities_zip = zip(dishes,countries)
print(list(country_specialities_zip))
country_specialities_dict = dict(country_specialities_zip)
print(country_specialities_dict)

"""
Exercises
Exercise 1
Write a function dict_merge_sum that takes two dictionaries d1 and d2 as parameters. The values of both dictionaries are numerical. The function should return the merged sum dictionary m of those dictionaries. If a key k is both in d1 and d2, the corresponding values will be added and included in the dictionary m If k is only contained in one of the dictionaries, the k and the corresponding value will be included in m

Exercise 2
Given is the following simplified data of a supermarket:

supermarket = { "milk": {"quantity": 20, "price": 1.19},
               "biscuits":  {"quantity": 32, "price": 1.45},
               "butter":  {"quantity": 20, "price": 2.29},
               "cheese":  {"quantity": 15, "price": 1.90},
               "bread":  {"quantity": 15, "price": 2.59},
               "cookies":  {"quantity": 20, "price": 4.99},
               "yogurt": {"quantity": 18, "price": 3.65},
               "apples":  {"quantity": 35, "price": 3.15},
               "oranges":  {"quantity": 40, "price": 0.99},
               "bananas": {"quantity": 23, "price": 1.29}}
To be ready for an imminent crisis you decide to buy everything. This isn't particularly social behavior, but for the sake of the task, let's imagine it. The question is how much will you have to pay?

Exercise 3
Create a virtual supermarket. For every article there is a price per article and a quantity, i.e. the stock. (Hint: you can use the one from the previous exercise!)
Create shopping lists for customers. The shopping lists contain articles plus the quantity.
The customers fill their carts, one after the other. Check if enough goods are available! Create a receipt for each customer.
Exercise 4
Given is the island of Vannoth

Island with fake Cities

Create a dictionary, where we get for every city of Vannoth the distance to the capital city of Rogeburgh

Exercise 5
Create a dictionary where you can get the distance between two arbitrary cities

Solutions
Solution to Exercise 1
We offer two solutions to this exercise:

The first one is only using things you will have learned, if you followed our Python course sequentially. The second solution uses techniques which will be covered later in our tutorial.

First solution:

def dict_merge_sum(d1, d2):
    
    Merging and calculating the sum of two dictionaries: 
    Two dicionaries d1 and d2 with numerical values and
    possibly disjoint keys are merged and the values are added if
    the exist in both values, otherwise the missing value is taken to
    be 0

    merged_sum = d1.copy()
    for key, value in d2.items():
        if key in d1:
            d1[key] += value
        else:
            d1[key] = value
    return merged_sum
d1 = dict(a=4, b=5, d=8)
d2 = dict(a=1, d=10, e=9)
dict_merge_sum(d1, d2)
Second solution:

def dict_sum(d1, d2):
    
    Merging and calculating the sum of two dictionaries: 
    Two dicionaries d1 and d2 with numerical values and
    possibly disjoint keys are merged and the values are added if
    the exist in both values, otherwise the missing value is taken to
    be 0

    return { k: d1.get(k, 0) + d2.get(k, 0) for k in set(d1) | set(d2) }
d1 = dict(a=4, b=5, d=8)
d2 = dict(a=1, d=10, e=9)
dict_merge_sum(d1, d2)
Solution to Exercise 2:
total_value = 0
for article in supermarket:
    quantity = supermarket[article]["quantity"]
    price = supermarket[article]["price"]
    total_value += quantity * price
print(f"The total price for buying everything: {total_value:7.2f}")
Solution to Exercise 3:
supermarket = { "milk": {"quantity": 20, "price": 1.19},
               "biscuits":  {"quantity": 32, "price": 1.45},
               "butter":  {"quantity": 20, "price": 2.29},
               "cheese":  {"quantity": 15, "price": 1.90},
               "bread":  {"quantity": 15, "price": 2.59},
               "cookies":  {"quantity": 20, "price": 4.99},
               "yogurt": {"quantity": 18, "price": 3.65},
               "apples":  {"quantity": 35, "price": 3.15},
               "oranges":  {"quantity": 40, "price": 0.99},
               "bananas": {"quantity": 23, "price": 1.29}            
              }
customers = ["Frank", "Mary", "Paul"]
shopping_lists = { 
   "Frank" : [('milk', 5), ('apples', 5), ('butter', 1), ('cookies', 1)],
   "Mary":  [('apples', 2), ('cheese', 4), ('bread', 2), ('pears', 3), 
             ('bananas', 4), ('oranges', 1), ('cherries', 4)],
   "Paul":  [('biscuits', 2), ('apples', 3), ('yogurt', 2), ('pears', 1), 
             ('butter', 3), ('cheese', 1), ('milk', 1), ('cookies', 4)]}
# filling the carts
carts = {}
for customer in customers:
    carts[customer] = []
    for article, quantity in shopping_lists[customer]:
        if article in supermarket:
            if supermarket[article]["quantity"] < quantity:
                quantity = supermarket[article]["quantity"]
            if quantity:
                supermarket[article]["quantity"] -= quantity
                carts[customer].append((article, quantity))
for customer in customers:                            
     print(carts[customer])
print("checkout")
for customer in customers:
    print("\ncheckout for " + customer + ":")
    total_sum = 0
    for name, quantity in carts[customer]:
        unit_price = supermarket[name]["price"]
        item_sum = quantity * unit_price
        print(f"{quantity:3d} {name:12s} {unit_price:8.2f} {item_sum:8.2f}")
        total_sum += item_sum
    print(f"Total sum:             {total_sum:11.2f}")
Alternative solution to exercise 3, in which we create the chopping lists randomly:

import random
supermarket = { "milk": {"quantity": 20, "price": 1.19},
               "biscuits":  {"quantity": 32, "price": 1.45},
               "butter":  {"quantity": 20, "price": 2.29},
               "cheese":  {"quantity": 15, "price": 1.90},
               "bread":  {"quantity": 15, "price": 2.59},
               "cookies":  {"quantity": 20, "price": 4.99},
               "yogurt": {"quantity": 18, "price": 3.65},
               "apples":  {"quantity": 35, "price": 3.15},
               "oranges":  {"quantity": 40, "price": 0.99},
               "bananas": {"quantity": 23, "price": 1.29}            
              }
articles4shopping_lists = list(supermarket.keys()) + ["pears", "cherries"]
max_articles_per_customer = 5 # not like a real supermarket :-)
customers = ["Frank", "Mary", "Paul", "Jennifer"]
shopping_lists = {}
for customer in customers:
    no_of_items = random.randint(1, len(articles4shopping_lists))
    shopping_lists[customer] = []
    for article_name in random.sample(articles4shopping_lists, no_of_items):
        quantity = random.randint(1, max_articles_per_customer)
        shopping_lists[customer].append((article_name, quantity))
# let's look at the shopping lists
print("Shopping lists:")        
for customer in customers:     
    print(customer + ":  " + str(shopping_lists[customer]))
# filling the carts
carts = {}
for customer in customers:
    carts[customer] = []
    for article, quantity in shopping_lists[customer]:
        if article in supermarket:
            if supermarket[article]["quantity"] < quantity:
                quantity = supermarket[article]["quantity"]
            if quantity:
                supermarket[article]["quantity"] -= quantity
                carts[customer].append((article, quantity))
print("\nCheckout")
for customer in customers:
    print("\ncheckout for " + customer + ":")
    total_sum = 0
    for name, quantity in carts[customer]:
        unit_price = supermarket[name]["price"]
        item_sum = quantity * unit_price
        print(f"{quantity:3d} {name:12s} {unit_price:8.2f} {item_sum:8.2f}")
        total_sum += item_sum
    print(f"Total sum:             {total_sum:11.2f}")
Solution to Exercise 4:
rogerburgh = {'Smithstad': 5.2, 'Scottshire': 12.3, 'Clarkhaven': 14.9, 'Dixonshire': 12.7, 'Port Carol': 3.4}
Solution to Exercise 5:
distances = {'Rogerburgh': {'Smithstad': 5.2, 'Scottshire': 12.3, 'Clarkhaven': 14.9, 'Dixonshire': 12.7, 'Port Carol': 3.4},
             'Smithstad': {'Rogerburh': 5.2, 'Scottshire': 11.1, 'Clarkhaven': 19.1, 'Dixonshire': 17.9, 'Port Carol': 8.6},
             'Scottshire': {'Smithstad': 11.1, 'Rogerburgh': 12.3, 'Clarkhaven': 18.1, 'Dixonshire': 19.3, 'Port Carol': 15.7},
             'Clarkshaven': {'Smithstad': 19.1, 'Scottshire': 18.1, 'Rogerburgh': 14.9, 'Dixonshire': 6.8, 'Port Carol': 17.1},
             'Dixonshire': {'Smithstad': 5.2, 'Scottshire': 12.3, 'Clarkhaven': 14.9, 'Rogerburg': 12.7, 'Port Carol': 16.1},
             'Port Carol': {'Smithstad': 8.6, 'Scottshire': 15.7, 'Clarkhaven': 17.1, 'Dixonshire': 16.1, 'Rogerburgh': 3.4}     
            }

"""