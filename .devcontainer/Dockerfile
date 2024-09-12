FROM --platform=linux/arm64 ubuntu:24.04

RUN dpkg --add-architecture amd64
RUN cat > /etc/apt/sources.list.d/amd64.list <<EOF
deb [arch=amd64] http://archive.ubuntu.com/ubuntu/ noble main restricted universe multiverse
deb [arch=amd64] http://archive.ubuntu.com/ubuntu/ noble-updates main restricted universe multiverse
deb [arch=amd64] http://archive.ubuntu.com/ubuntu/ noble-security main restricted universe multiverse
deb [arch=amd64] http://archive.ubuntu.com/ubuntu/ noble-backports main restricted universe multiverse
EOF

RUN rm /etc/apt/sources.list.d/ubuntu.sources && cat > /etc/apt/sources.list.d/arm64.list <<EOF
deb [arch=arm64] http://ports.ubuntu.com/ubuntu-ports/ noble main restricted universe multiverse
deb [arch=arm64] http://ports.ubuntu.com/ubuntu-ports/ noble-updates main restricted universe multiverse
deb [arch=arm64] http://ports.ubuntu.com/ubuntu-ports/ noble-security main restricted universe multiverse
deb [arch=arm64] http://ports.ubuntu.com/ubuntu-ports/ noble-backports main restricted universe multiverse
EOF

RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y qemu-user python3 python3-pwntools libc6:amd64 gdb-multiarch git tmux

WORKDIR /opt
RUN git clone https://github.com/pwndbg/pwndbg && cd pwndbg && ./setup.sh

RUN echo -n '#!/bin/bash\necho "$@" > /tmp/pwntoolscode-dbgcmd' > /opt/pwntools-fake-term.sh && chmod +x /opt/pwntools-fake-term.sh

WORKDIR /root
