FROM python:3.11

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip3 install --default-timeout=1000 --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./app.py" ]