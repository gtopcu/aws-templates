# API GW HTTP Rest API with Cognito JWT Auth

import http.client
import threading
import time

exitFlag = 0
"""
conn = http.client.HTTPSConnection("izb9erxhx4.execute-api.us-east-2.amazonaws.com")
payload = ""
#headers = { 'Authorization': "Bearer eyJraWQiOiJhR0F1aDdraVNzMEt5XC9YeHp1VXN6eGgrSEZ0WkZ1SHFLQXBWdlkxOUU1ND0iLCJhbGciOiJSUzI1NiJ9.eyJvcmlnaW5fanRpIjoiNDVhMTA5MDgtYzgxYi00NTlmLTlmYjQtY2Y5NGY2YTkyYzRkIiwic3ViIjoiYmMxMDU5NWQtZGQ4Ni00ZGIwLTkzODQtM2MxM2M5NDEzMTgwIiwiZXZlbnRfaWQiOiI3ZGFhYTIwMy00MDNhLTRjZjEtYTVhNS1mZDFlMjdhMWVjMjEiLCJ0b2tlbl91c2UiOiJhY2Nlc3MiLCJzY29wZSI6ImF3cy5jb2duaXRvLnNpZ25pbi51c2VyLmFkbWluIiwiYXV0aF90aW1lIjoxNjQ4MDM1OTQ2LCJpc3MiOiJodHRwczpcL1wvY29nbml0by1pZHAudXMtZWFzdC0yLmFtYXpvbmF3cy5jb21cL3VzLWVhc3QtMl9RdHI0TjF5VnciLCJleHAiOjE2NDgwNzE5NDYsImlhdCI6MTY0ODAzNTk0NiwianRpIjoiMzI1OGZjM2ItOWU0Ny00YWI2LThkOTUtZjNiMzgxOTRiNTMxIiwiY2xpZW50X2lkIjoiNm1uOXJlMXZtazRrYTJvNGwzMXJ1anE4N2giLCJ1c2VybmFtZSI6ImJjMTA1OTVkLWRkODYtNGRiMC05Mzg0LTNjMTNjOTQxMzE4MCJ9.YKGjnFbegY2Y92WN3WfiR_O5k9RCn5dJJpf-FJj6m6MyVhVQD-rFjWx46ks8D8hYmf21wGbwraN16n4Q44aZ0QRtdsF1Br8t9J7vtONRWUVsRnN1mqvmbIEz4XiYNkC9zZfSealFtpDu95Ri382tJX8QJ5EIzrFYxfo1HDLAjvfaZnmxJxNSTdAvpeVoXBDOgo-HEBvd_HHzkvHDR0rv-mXEc1rydqH2zW0i9J0Wgfrb-YthqZaO0EO_qwCmwU1qs0Wn4-Sw2_wSftX4R1kEQ3smUpMUfFwy3Y0iTOFT5gJcUMfijkq4lhFJK0jg9dq9op8ZbT1GPvfMJnoAPG8LSQ" }
#conn.request("GET", "/00_infraops_donotdelete", payload, headers)
for i in range(0, 100):
    conn.request("GET", "/00_infraops_donotdelete")
    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))
"""

threadCount = 5
loopCount = 100

class myThread(threading.Thread):
   def __init__(self, threadID, name):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
   def run(self):
      print("Thread Starting " + self.name)
      conn = http.client.HTTPSConnection("izb9erxhx4.execute-api.us-east-2.amazonaws.com")
      for i in range(0, loopCount):
          conn.request("GET", "/00_infraops_donotdelete")
          res = conn.getresponse()
          data = res.read()
          print(data.decode("utf-8"))
      print("Thread Exiting " + self.name)

# Create new threads
for i in range(0, threadCount):
    thread = myThread(i, "Thread-" + str(i))
    thread.start()

print("\nActive thread count: ", threading.active_count())
#print(threading.enumerate())