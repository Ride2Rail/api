# base image
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

# set maintainer (MAINTAINER is deprecated)
# See:
#   https://docs.docker.com/engine/reference/builder/#maintainer-deprecated
LABEL maintainer="cristian.consonni@eurecat.org"

# upgrade pip
RUN pip3 install --no-cache-dir --upgrade pip

COPY ./requirements.txt /requirements.txt

RUN pip install --no-cache-dir -r /requirements.txt

COPY ./app /app

# copy directory with protobuf definitions
COPY ./proto/r2r /app/r2r

WORKDIR /app
