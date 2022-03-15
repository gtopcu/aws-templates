#!/usr/bin/python3

# 1. Python env has to be added as the first line of your file
# #!/usr/bin/env python3 (linux) 
# #!/usr/bin/python3 (mac)
 
# 2. The file has to be made executable: 
# chmod +x awsCLIBash.py or
# chmod 755 awsCLIBash.py
# verify by: ls -ltr awsCLIBash.py

# 3. Run:
# ./awsCLIBash.py 1 2

import os
import sys

exitFlag = 0

#os.system("clear") # Linux - OSX
#os.system("cls") # Windows

""""
print("Congrats, I'm running as bash!")

print(sys.argv[0])
for eachArg in sys.argv:   
        print(eachArg)
"""

updateStr = "aws dynamodb update-continuous-backups \
    --table-name {} \
    --point-in-time-recovery-specification PointInTimeRecoveryEnabled=true \
    --profile spiky"

with open("tableList.txt", "r") as fh:
    for line in fh:
        #print(updateStr.format(line.strip()))
        os.system(updateStr.format(line.strip()))


        
