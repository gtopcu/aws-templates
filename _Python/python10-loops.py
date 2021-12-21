# https://python-course.eu/python-tutorial/conditional-statements.php
# https://python-course.eu/python-tutorial/loops.php
# https://python-course.eu/python-tutorial/for-loop.php

# for: collection-controolled loop
# while: condition-controlled loop

# !! Avoid changing the list in the loop body - work on a copy instead !!

# If
person = "Nationality?"
if person == "french" or person == "French":
    print("Préférez-vous parler français?")
elif person == "italian" or person == "Italian":
    print("Preferisci parlare italiano?")
else:
    print("You are neither French nor Italian.")

for i in range(0, 10):
    print(i)
    if(i == 5):
        break

# Ternary If
inside_city_limits = True
maximum_speed = 50 if inside_city_limits else 100
print(maximum_speed)


# While

counter = 0
while counter in range(0, 3):
    print(counter, sep=":", end=" ")
    counter = counter+1
# The statements in the else part are executed when the condition is not fulfilled anymore:
else:
    print("interesting while?")
print("Done")


# If a loop is left by break, the else part is not executed
# Use continue to skip to the next interation

import random
upper_bound = 20
lower_bound = 1
#to_be_guessed = int(n * random.random()) + 1
to_be_guessed = random.randint(lower_bound, upper_bound)
guess = 0
while guess != to_be_guessed:
    guess = int(input("Guess the number: "))
    if guess > 0:
        if guess > to_be_guessed:
            print("Number too large")
        elif guess < to_be_guessed:
            print("Number too small")
    else:
        # 0 means giving up
        print("Sorry that you're giving up!")
        break   # break out of a loop, don't execute "else"
else:
    print("Congratulations. You made it!!")

