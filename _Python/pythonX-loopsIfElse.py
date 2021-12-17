# https://python-course.eu/python-tutorial/conditional-statements.php

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

counter = 0
while counter in range(0, 3):
    print(counter, sep=":", end=" ")
    counter = counter+1
else:
    print("interesting while?")

print("Done")
