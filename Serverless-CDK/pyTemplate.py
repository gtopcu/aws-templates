
import os
import sys
import json
import random
import logging

#logging.basicConfig()
logger = logging.getLogger()
logger.setLevel(logging.INFO)

os.system("clear") # Linux - OSX
#os.system("cls") # Windows
for arg in sys.argv:   
        print(arg)

if __name__ == '__main__':
    logging.info("Sample log")
    print("running")

print("Done!")