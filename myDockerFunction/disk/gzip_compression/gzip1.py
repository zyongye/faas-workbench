from time import time
import os
import gzip


def main(request):
    file_size = request['file_size']
    file_write_path = './file'

    start = time()
    with open(file_write_path, 'wb') as f:
        f.write(os.urandom(file_size * 1024 * 1024))
    disk_latency = time() - start

    with open(file_write_path) as f:
        start = time()
        with gzip.open('./result', 'wb') as gz:
            gz.writelines(f)
        compress_latency = time() - start

    return { "disk_latency": str(disk_latency),
             "compress_latency": str(compress_latency) }

main({"file_size": 1})
