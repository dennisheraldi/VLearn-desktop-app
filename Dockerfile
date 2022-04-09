FROM python:3.7.13-alpine

WORKDIR /usr/app

COPY . ./

RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "./main.py" ]