FROM openwhisk/python3action:latest
RUN apk add --update py-pip
COPY . /faas
RUN pip install -r /faas/requirements.txt
