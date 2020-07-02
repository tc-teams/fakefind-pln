FROM python:3.7 as builder

RUN apt-get update && apt-get install -y --no-install-recommends gcc build-essential

RUN mkdir /build

ADD . /build/

WORKDIR /build

RUN pip3 install flask && flask_restful && nltk

FROM python:3.7 

COPY --from=builder /build/main /app/

WORKDIR /app

EXPOSE 8080

CMD ["python","main.py"]