FROM centos:centos8

SHELL ["/bin/bash", "-c"]
#Python Install

RUN dnf -y install python36

#fastText Build

RUN dnf install -y git make gcc gcc-c++
RUN dnf install -y python36-devel
WORKDIR /usr/local/src
RUN git clone https://github.com/facebookresearch/fastText.git
WORKDIR /usr/local/src/fastText
RUN pip3 install .

#Install Python Package
RUN pip3 install numpy pandas matplotlib scikit-learn
RUN rpm -ivh http://packages.groonga.org/centos/groonga-release-1.1.0-1.noarch.rpm
RUN dnf -y makecache
RUN dnf -y install --nogpgcheck mecab mecab-ipadic mecab-devel
RUN pip3 install mecab-python3 neologdn emoji

RUN mkdir -p /root/home
WORKDIR /root/home

#Install Mecab Dictionary

# RUN yum install -y diffutils patch which file openssl
# 
# WORKDIR /usr/local/src
# RUN git clone --depth 1 https://github.com/neologd/mecab-ipadic-neologd.git
# WORKDIR /usr/local/src/mecab-ipadic-neologd
# RUN ./bin/install-mecab-ipadic-neologd -n -y