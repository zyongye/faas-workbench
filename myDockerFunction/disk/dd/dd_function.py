import os
import subprocess


def main(request):
    bs = 'bs='+str(request['bs'])
    count = 'count='+str(request['count'])
    print(bs)
    print(count)
    out_fd = open('/tmp/io_write_logs','w')
    a = subprocess.Popen(['dd', 'if=/dev/zero', 'of=/tmp/out', bs, count], stderr=out_fd)
    a.communicate()
    
    output = subprocess.check_output(['ls', '-alh', '/tmp/'])
    print(output)

    output = subprocess.check_output(['du', '-sh', '/tmp/'])
    print(output)
                               
    with open('/tmp/io_write_logs') as logs:
        result = { 'body': str(logs.readlines()).replace('\n', '') }
        print(result)
        return result

