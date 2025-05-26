
# https://www.youtube.com/watch?v=SOu6hgklQRA

# pip install locust
# locust -f locustio.py
# http://localhost:8089
# locust -f locustio.py --host http://localhost:5000 --users 50 --spawn-rate 10

from locust import HttpUser, FastHttpUser, task, between, TaskSet, User

# class LoadUser(HttpUser):
class LoadUser(FastHttpUser):
    
    wait_time = between(1, 3)
    # each spawned user picks a random task
    
    @task
    def home_page(self):
        self.client.get(url="/home")
        # self.client.put()
        # self.client.post()
        # self.client.patch()
        # self.client.delete()

    @task
    def about_page(self):
        self.client.get(url="/about")