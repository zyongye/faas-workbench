from time import time
import random
import string
import pyaes


def generate(length):
    letters = string.ascii_lowercase + string.digits
    return ''.join(random.choice(letters) for i in range(length))


def main(request):
    length_of_message = request["length_of_message"]
    num_of_iterations = request["num_of_iterations"]

    message = generate(int(length_of_message))

    # 128-bit key (16 bytes)
    KEY = b'\xa1\xf6%\x8c\x87}_\xcd\x89dHE8\xbf\xc9,'

    start = time()
    for loops in range(int(num_of_iterations)):
        aes = pyaes.AESModeOfOperationCTR(KEY)
        ciphertext = aes.encrypt(message)
        print(ciphertext)

        aes = pyaes.AESModeOfOperationCTR(KEY)
        plaintext = aes.decrypt(ciphertext)
        print(plaintext)
        aes = None

    latency = time() - start

    return { "body": {"latency": str(latency)} } 
