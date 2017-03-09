FROM ubuntu:16.04

#=======================
# General Configuration
#=======================
RUN apt-get update -y

#==================
# Install Python 3
#==================
RUN apt-get install python3 python3-pip -y

#======================
# Install dependencies
#======================
COPY requirements.txt /tmp/
RUN pip3 install -r /tmp/requirements.txt

#==============================
# Install Supervisor and Nginx
#==============================
RUN apt-get install supervisor nginx -y
ENV LOG_PATH=/var/log/supervisor
COPY nginx/nginx.conf /etc/nginx/

#=============
# Expose Port
#=============
EXPOSE 80

#=========
# Run app
#=========
COPY . /opt/
WORKDIR /opt
CMD /usr/bin/supervisord --configuration supervisord.conf
