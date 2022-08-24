FROM python:3.8

ENV PATH="${PATH}:/root/.poetry/bin"

WORKDIR /var/try-to-SqlAlchemy
ADD . /var/try-to-SqlAlchemy

RUN python -m pip install --upgrade pip
RUN pip install sqlalchemy
RUN pip install pymysql
