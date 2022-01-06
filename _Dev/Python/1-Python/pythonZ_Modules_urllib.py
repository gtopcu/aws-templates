"""
https://docs.python.org/3/library/urllib.request.html
https://www.geeksforgeeks.org/python-urllib-module/

urllib.request for opening and reading.
urllib.error for the exceptions raised
urllib.parse for parsing URLs
urllib.robotparser for parsing robot.txt files

If urllib is not present in your environment, execute the below code to install it.
pip install urllib

urllib.request.urlopen(url, data=None, [timeout, ]*, cafile=None, capath=None, cadefault=False, context=None)
class urllib.request.Request(url, data=None, headers={}, origin_req_host=None, unverifiable=False, method=None)
"""

import time
#import urllib.request, urllib.response, urllib.parse, urllib.error

# urllib.request
# For HTTP and HTTPS URLs, this function returns a http.client.HTTPResponse 
import urllib.request
now = time.time()
request_url = urllib.request.urlopen("http://www.http2demo.io/")
print(time.time() - now)
# print(request_url.read())

#urllib.error
# This module defines the classes for exception raised by urllib.request. Whenever there is an error in 
# fetching a URL, this module helps in raising exceptions. The following are the exceptions raised :
#   - URLError – It is raised for the errors in URLs, or errors while fetching the URL due to connectivity, 
#   and has a ‘reason’ property that tells a user the reason of error.
#   - HTTPError – It is raised for the exotic HTTP errors, such as the authentication request errors. 
#   It is a subclass or URLError. Typical errors include ‘404’ (page not found), ‘403’ (request forbidden),
#   and ‘401’ (authentication required).
#import urllib.request
#import urllib.parse
  
# trying to read the URL but with no internet connectivity
try:
    x = urllib.request.urlopen('https://www.google.com')
    print(x.read())
# Catching the exception generated     
except Exception as e :
     print(str(e))

# urllib.parse
# Helps to define functions to manipulate URLs and their components parts, to build or break them. 
# Focuses on splitting a URL into small components; or joining different URL components into URL strings.
from urllib.parse import * 
parse_url = urlparse('https://www.geeksforgeeks.org/python-langtons-ant?test=1')
print(parse_url)
print("\n")
unparse_url = urlunparse(parse_url)
print(unparse_url)



