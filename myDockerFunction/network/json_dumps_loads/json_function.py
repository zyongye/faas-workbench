from time import time
import json
from urllib.request import urlopen


def main(request):
    link = request['link'] # https://github.com/jdorfman/awesome-json-datasets

    start = time()
    f = urlopen(link)
    data = f.read().decode("utf-8")
    network = time() - start

    start = time()
    json_data = json.loads(data)
    str_json = json.dumps(json_data, indent=4)
    latency = time() - start

    print(str_json)

    return { "network": str(network),
             "latency": str(latency) }

