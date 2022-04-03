from locust import HttpUser, task, events, constant
import warnings
import random

@events.init.add_listener
def on_locust_init(environment, **kwargs):
    warnings.filterwarnings("ignore")


class OpenWhiskUser(HttpUser):
    wait_time = constant(3)
    
    @task
    def floatOp(self):
        N = random.randint( -2**15 , 2**15 - 1)
        self.client.get("/api/v1/web/guest/default/floatOp.http?N=%d" % N, verify=False)

    @task
    def matmul(self):
        N = random.randint( 0, 2**10)
        self.client.get("/api/v1/web/guest/default/matmul.http?N=%d" % N, verify=False)

    @task
    def linpack(self):
        N = random.randint( 0, 2**10)
        self.client.get("/api/v1/web/guest/default/linpack.http?N=%d" % N, verify=False)
    
    @task
    def pyaes(self):
        length_of_message = random.randint( 1, 2**15)
        num_of_iterations = random.randint( 0, 100)
        self.client.get("/api/v1/web/guest/default/pyaes.http?length_of_message=%d&num_of_iterations=%d" % (length_of_message, num_of_iterations), verify=False)

    @task
    def dd(self):
        bs = random.randint( 0, 2**15)
        count = random.randint(0, 100)
        self.client.get("/api/v1/web/guest/default/dd.http?bs=%d&count=%d" % (bs, count), verify=False)

    @task
    def json_f(self):
        link = 'https://api.nobelprize.org/v1/prize.json'
        self.client.get("/api/v1/web/guest/default/json.http?link=%s" % link, verify=False)
