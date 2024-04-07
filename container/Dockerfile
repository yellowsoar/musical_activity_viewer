# https://hub.docker.com/_/python/tags?page=1&name=3.12
FROM python:3.12.2-slim-bookworm

# Install debian packages
RUN apt-get update \
    && apt-get install \
    -y --no-install-recommends \
    apache2 \
    && apt-get autoclean

# Install Python Packages
COPY src/requirements.txt /tmp/
WORKDIR /tmp
RUN pip install \
        --no-cache-dir \
        -r requirements.txt \
        && rm -rf /tmp/requirements*

# Install non-project Python Packages
RUN pip install \
        --no-cache-dir \
        sqlite-web \
        supervisor

COPY reverse_proxy/mav.conf /etc/apache2/sites-available
COPY reverse_proxy/apache2.conf /etc/apache2/apache2.conf
COPY supervisord.conf /tmp/supervisord.conf
COPY container/docker-entrypoint.sh /tmp/docker-entrypoint.sh
COPY src /web

EXPOSE 80
ENV PYTHONUNBUFFERED=1

WORKDIR /web
ENTRYPOINT ["bash", "/tmp/docker-entrypoint.sh"]
