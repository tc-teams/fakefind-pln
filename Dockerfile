FROM python:3.8

RUN apt-get update && apt-get install -y --no-install-recommends gcc build-essential

WORKDIR /code

COPY requirements.txt .

RUN pip3 install -r requirements.txt
RUN python3 -m nltk.downloader stopwords
RUN python3 -m nltk.downloader rslp
RUN python3 -m nltk.downloader punkt

COPY . .

EXPOSE 80

CMD ["python","sample.py","runserver","--port", "80","--host","0.0.0.0"]
