FROM python:2.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /myproj
WORKDIR /myproj
ADD requirements.txt /myproj/
RUN pip install -r requirements.txt
ADD . /myproj/
