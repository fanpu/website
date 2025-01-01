<<<<<<< HEAD
<<<<<<< HEAD
FROM ruby:slim

# uncomment these if you are having this issue with the build:
# /usr/local/bundle/gems/jekyll-4.3.4/lib/jekyll/site.rb:509:in `initialize': Permission denied @ rb_sysopen - /srv/jekyll/.jekyll-cache/.gitignore (Errno::EACCES)
# ARG GROUPID=901
# ARG GROUPNAME=ruby
# ARG USERID=901
# ARG USERNAME=jekyll

ENV DEBIAN_FRONTEND noninteractive

LABEL authors="Amir Pourmand,George Araújo" \
    description="Docker image for al-folio academic template" \
    maintainer="Amir Pourmand"

# uncomment these if you are having this issue with the build:
# /usr/local/bundle/gems/jekyll-4.3.4/lib/jekyll/site.rb:509:in `initialize': Permission denied @ rb_sysopen - /srv/jekyll/.jekyll-cache/.gitignore (Errno::EACCES)
# add a non-root user to the image with a specific group and user id to avoid permission issues
# RUN groupadd -r $GROUPNAME -g $GROUPID && \
#     useradd -u $USERID -m -g $GROUPNAME $USERNAME

# install system dependencies
RUN apt-get update -y && \
    apt-get install -y --no-install-recommends \
<<<<<<< HEAD
    build-essential \
    curl \
    git \
    imagemagick \
    inotify-tools \
    locales \
    nodejs \
    procps \
    python3-pip \
    zlib1g-dev && \
=======
        build-essential \
        curl \
        git \
        imagemagick \
        inotify-tools \
        locales \
        nodejs \
        procps \
        python3-pip \
        zlib1g-dev && \
>>>>>>> a3396b6c (Updated ffi, changed base docker image, added observer and ostruct (#2931))
    pip --no-cache-dir install --upgrade --break-system-packages nbconvert

# clean up
RUN apt-get clean && \
    apt-get autoremove && \
    rm -rf /var/lib/apt/lists/* /var/cache/apt/archives/*  /tmp/*

# set the locale
=======
FROM bitnami/minideb:latest
=======
FROM ubuntu:latest
ENV DEBIAN_FRONTEND noninteractive
>>>>>>> 6b5c94f5716c3ce857b0ddf7409e0de5e4e7f6fa

Label MAINTAINER Amir Pourmand

RUN apt-get update -y && apt-get install -y --no-install-recommends \
    locales \
    imagemagick \
    ruby-full \
    build-essential \
    zlib1g-dev \
    jupyter-nbconvert \
    inotify-tools procps && \
    apt-get clean && rm -rf /var/lib/apt/lists/* /var/cache/apt/archives/*


<<<<<<< HEAD
# add locale
RUN apt-get -y install locales
# Set the locale
>>>>>>> c8ebb5c289b6ee987ea06b7cde0a3db2237862c0
=======
>>>>>>> 6b5c94f5716c3ce857b0ddf7409e0de5e4e7f6fa
RUN sed -i '/en_US.UTF-8/s/^# //g' /etc/locale.gen && \
    locale-gen


ENV LANG=en_US.UTF-8 \
    LANGUAGE=en_US:en \
    LC_ALL=en_US.UTF-8 \
    JEKYLL_ENV=production

# install jekyll and dependencies
RUN gem install jekyll bundler

RUN mkdir /srv/jekyll

ADD Gemfile /srv/jekyll

WORKDIR /srv/jekyll

RUN bundle install --no-cache
# && rm -rf /var/lib/gems/3.1.0/cache
EXPOSE 8080

COPY bin/entry_point.sh /tmp/entry_point.sh

CMD ["/tmp/entry_point.sh"]
