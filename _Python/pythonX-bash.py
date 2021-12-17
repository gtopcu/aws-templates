#!/usr/bin/python3

# 1. Python env has to be added as the first line of your file
# #!/usr/bin/env python3 (linux) 
# #!/usr/bin/python3 (mac)
 
# 2. The file has to be made executable: 
# chmod +x scriptname.py or
# chmod 755 scriptname.py
# verify by: ls -ltr scriptname.py

# 3. Run:
# ./scriptname.py

import os
os.system("clear") # Linux - OSX
#os.system("cls") # Windows

print("Congrats, I'm running as bash!")