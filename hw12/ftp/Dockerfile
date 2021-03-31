FROM ubuntu:18.04
RUN mkdir /opt/app
RUN mkdir /opt/data
WORKDIR /opt/data
VOLUME /opt/data
EXPOSE 223

COPY start.sh /opt/data/start.sh
COPY ps.py /opt/data/ps.py
COPY vsftpd.conf /etc/vsftpd/vsftpd.conf
COPY ssh_config /etc/ssh/sshd_config

RUN apt-get update -y && \
apt-get install vsftpd -y && \
apt-get install ftp -y && \
apt-get install sshpass -y

RUN bash start.sh

RUN apt-get update && apt-get install -y \
	openssh-server \
	mcrypt \
	&& mkdir /var/run/sshd \
	&& chmod 0755 /var/run/sshd \
	&& mkdir -p /data/incoming \
	&& apt-get clean \
	&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \
	&& mkdir /ssh/
	
ENTRYPOINT ["/bin/bash", "/opt/data/python ps.py"]
