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

COPY src /web
# Install non-project Python Packages
RUN pip install \
        --no-cache-dir \
        sqlite-web \
        supervisor

COPY reverse_proxy/mav.conf /etc/apache2/sites-available
COPY container/docker-entrypoint.sh /web/docker-entrypoint.sh
COPY reverse_proxy/apache2.conf /etc/apache2/apache2.conf
COPY supervisord.conf /tmp/supervisord.conf

EXPOSE 80
ENV PYTHONUNBUFFERED=1

WORKDIR /web
ENTRYPOINT ["bash", "docker-entrypoint.sh"]
