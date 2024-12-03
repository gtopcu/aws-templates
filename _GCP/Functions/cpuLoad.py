

# https://medium.com/google-cloud/optimize-your-cloud-run-functions-7bf0b6c188f4
# HTTP Cloud Function - Loads CPU by calculating SHA512 hashes

# main.py
import functions_framework
import random
import string
from datetime import datetime
import hashlib

N = 51200

@functions_framework.http
def hello_http(request):

    m = hashlib.sha512()
    # Generate a random long string
    rstr = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(N))
    # print(rstr)

    t1 = datetime.now()
    print("Start time: " + str(t1))

    # repeatedly compute the digest
    for i in range(100000):
        m.update(rstr.encode())
        digest:bytes = m.digest()
        # print(digest.hex())
        # print(digest.upper())

    t2 = datetime.now()
    print("End time: " + str(t2))
    print("Difference: " + str(t2 - t1))

    difference = str(t2 - t1)

    return 'Performance {}!'.format(difference)

if __name__ == '__main__':
    hello_http(None)




# N = 51200

# # This function is called during cold start only
# def computeHashes():
#     m = hashlib.sha512()
#     # Generate a random long string
#     rstr = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(N))

#     t1 = datetime.now()
#     print("Start time: " + str(t1))

#     # repeatedly compute the digest
#     for i in range(10000):
#         m.update(rstr.encode())
#         m.digest()

#     t2 = datetime.now()
#     print("End time: " + str(t2))
#     print("Difference: " + str(t2 - t1))

#     difference = str(t2 - t1)
#     return difference

# # Save results in global state    
# perf = computeHashes()

# @functions_framework.http
# def hello_http(request):

#     return 'Performance {}!'.format(perf)