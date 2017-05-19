FROM python:2.7

#Install Tor
RUN echo "deb http://deb.torproject.org/torproject.org jessie main" >> /etc/apt/sources.list
RUN echo "deb-src http://deb.torproject.org/torproject.org jessie main" >> /etc/apt/sources.list
RUN gpg --keyserver keys.gnupg.net --recv A3C4F0F979CAA22CDBA8F512EE8CBC9E886DDD89
RUN gpg --export A3C4F0F979CAA22CDBA8F512EE8CBC9E886DDD89 | apt-key add -
RUN apt-get update
RUN apt-get install -y tor deb.torproject.org-keyring


COPY src /src

RUN pip install -r /src/requirements.txt


ENTRYPOINT ["python", "/src/main.py"]