FROM ubuntu:18.04
RUN mkdir /opt/app
RUN mkdir /opt/data
WORKDIR /opt/data
VOLUME /opt/data
EXPOSE 223

COPY vsftpd.conf /etc/vsftpd/vsftpd.conf
# COPY ssh_config /etc/ssh/sshd_config

RUN mkdir /var/run/sshd && \
    mkdir /root/.ssh

RUN apt-get update && \
    apt-get install -y openssh-server

RUN echo 'root:root' |chpasswd

RUN sed -ri 's/^#?PermitRootLogin\s+.*/PermitRootLogin yes/' /etc/ssh/sshd_config
RUN sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config


RUN apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

CMD ["/usr/sbin/sshd", "-D"]