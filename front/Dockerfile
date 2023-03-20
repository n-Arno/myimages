FROM python:alpine

LABEL org.opencontainers.image.source=https://github.com/n-arno/myimages

RUN pip install bottle paste requests

COPY run.py /run.py

EXPOSE 80

ENTRYPOINT ["/run.py"]
