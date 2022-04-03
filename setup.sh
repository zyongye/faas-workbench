#!/bin/bash
wsk -i action create floatOp myDockerFunction/cpu-memory/float_operation/floatOp.py     --docker openwhisk/python3action --web true
wsk -i action create json    myDockerFunction/network/json_dumps_loads/json_function.py --docker openwhisk/python3action --web true
wsk -i action create matmul  myDockerFunction/cpu-memory/matmul/matmul.py               --docker zyy1102000/faas:matmul  --web true
wsk -i action create linpack myDockerFunction/cpu-memory/linpack/linpack.py             --docker zyy1102000/faas:linpack --web true
wsk -i action create pyaes   myDockerFunction/cpu-memory/pyaes/pyaes_function.py        --docker zyy1102000/faas:pyaes   --web true
wsk -i action create dd      myDockerFunction/disk/dd/dd_function.py                    --docker openwhisk/python3action --web true

