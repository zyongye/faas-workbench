import numpy as np
from time import time

def matmul(N):
    A = np.random.rand(N, N)
    B = np.random.rand(N, N)

    start = time()
    C = np.matmul(A, B)
    latency = time() - start

    return latency

def main(request):
    N = request['N']
    latency = matmul(int(N))
    print(latency)
    return { "body": {"latency": str(latency)}  }

