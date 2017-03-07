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

#=============
# Expose Port
#=============
EXPOSE 8080

#=========
# Run app
#=========
COPY . /opt/
WORKDIR /opt
ENV PYTHONPATH .
CMD python3 -m src.app
