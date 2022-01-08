
import sys

print(sys.argv[0])
for eachArg in sys.argv:   
        print(eachArg)

print("Error output", file=sys.stderr)
print("Standard output", file=sys.stdout)

