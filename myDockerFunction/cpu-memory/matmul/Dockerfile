FROM zyy1102000/faas:python3action 
RUN apk add --no-cache openblas-dev gcc libc-dev
COPY . /faas
RUN pip install -r /faas/requirements.txt
