FROM lkhagva/pwn:ubuntu-18.04

WORKDIR /home/pwn

ADD pwn ./
ADD flag ./
RUN chown pwn:pwn ./flag
RUN chmod 644 ./flag
RUN chown pwn:pwn ./pwn
RUN chmod 775 ./pwn

RUN useradd -s /bin/sh anonymous

ENTRYPOINT /docker-entrypoint.sh $VULN_PORT pwn
