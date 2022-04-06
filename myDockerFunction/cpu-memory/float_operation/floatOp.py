import math
from time import time
import os

def float_operation(N):
    start = time()
    for i in range(0, N):
        sin_i = math.sin(i)
        cos_i = math.cos(i)
        sqrt_i = math.sqrt(i)
    latency = time() - start
    return latency

def main(request):
    N = request['N']
    latency = float_operation(int(N))
    print(latency)
    return { "body": { "latency": str(latency) } }
