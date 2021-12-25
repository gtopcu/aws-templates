
# https://python-course.eu/python-tutorial/sets-examples.php

import re

# We don't care about case sensitivity and therefore use lower:
ulysses_txt = open("books/james_joyce_ulysses.txt").read().lower()

words = re.findall(r"\b[\w-]+\b", ulysses_txt)
print("The novel ulysses contains " + str(len(words)))

# Sum of all the words, together with the many words that occur multiple times:
for word in ["the", "while", "good", "bad", "ireland", "irish"]:
    print("The word '" + word + "' occurs " + \
          str(words.count(word)) + " times in the novel!" )

# Number of different words - now we need a set
diff_words = set(words)
print("'Ulysses' contains " + str(len(diff_words)) + " different words!")

# We will subtract all the words occurring in the other novels from "Ulysses": 
novels = ['sons_and_lovers_lawrence.txt', 
          'metamorphosis_kafka.txt', 
          'the_way_of_all_flash_butler.txt', 
          'robinson_crusoe_defoe.txt', 
          'to_the_lighthouse_woolf.txt', 
          'james_joyce_ulysses.txt', 
          'moby_dick_melville.txt']

words_in_novel = {}
for novel in novels:
    txt = open("books/" + novel).read().lower()
    words = re.findall(r"\b[\w-]+\b", txt)
    words_in_novel[novel] = words
    
words_only_in_ulysses =  set(words_in_novel['james_joyce_ulysses.txt'])
novels.remove('james_joyce_ulysses.txt')
for novel in novels:
    words_only_in_ulysses -= set(words_in_novel[novel])
    
with open("books/words_only_in_ulysses.txt", "w") as fh:
    txt = " ".join(words_only_in_ulysses)
    fh.write(txt)
    
print(len(words_only_in_ulysses))


# It is also possible to find the words which occur in every book. To accomplish this, 
# we need the set intersection:
common_words = set(words_in_novel['james_joyce_ulysses.txt'])
for novel in novels:
    common_words &= set(words_in_novel[novel])
print(len(common_words))

