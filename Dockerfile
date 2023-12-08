FROM python:3.8

ENV FLASK_APP=webapp
ENV FLASK_RUN_HOST=0.0.0.0

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["flask", "run"]
