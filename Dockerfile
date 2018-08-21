# use base python image with python 2.7
FROM python:2.7-alpine3.7
# RUN echo "http://dl-cdn.alpinelinux.org/alpine/edge/main" >> /etc/apk/repositories
RUN apk add --no-cache --repository http://dl-cdn.alpinelinux.org/alpine/edge/main \
  binutils \
  argon2 \
  nginx
RUN apk add --no-cache docker \
  libffi-dev \
  py-cffi \
  gcc \
  g++ \
  musl-dev \
  zlib-dev \
  jpeg-dev \
  freetype-dev \
  lcms2-dev \
  openjpeg-dev \
  tiff-dev \
  tk-dev \
  py-openssl \
  gfortran \
  tcl-dev \
  python-dev \
  py-pip \
  build-base \
  wget \
  openblas-dev \
  lapack \
  py-numpy \
  libxslt-dev \
  freetype-dev \
  chrony
  

RUN apk add --no-cache --repository  http://dl-cdn.alpinelinux.org/alpine/edge/community --repository http://dl-cdn.alpinelinux.org/alpine/edge/testing \
  py-scipy


RUN ln -s /usr/include/locale.h /usr/include/xlocale.h
