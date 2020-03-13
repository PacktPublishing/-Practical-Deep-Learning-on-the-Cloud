FROM amazonlinux:latest
RUN yum install -y python3
RUN pip3 install scipy boto3
COPY . /app
RUN chmod 777 -R /app