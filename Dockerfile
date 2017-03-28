FROM ubuntu:16.04

#==================
# General Packages
#==================
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    supervisor \
    nginx \
 && rm -rf /var/lib/apt/lists/*

#======================
# Install dependencies
#======================
COPY requirements.txt /tmp/
RUN pip3 install -r /tmp/requirements.txt

#=============
# Expose Port
#=============
EXPOSE 80

#=========
# Run app
#=========
WORKDIR /opt
COPY nginx/nginx.conf /etc/nginx/
COPY . /opt/
ENV LOG_PATH=/var/log/supervisor
CMD /usr/bin/supervisord --configuration supervisord.conf
