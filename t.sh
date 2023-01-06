#!/bin/bash
wget -P /usr/local/ https://mirrors.tuna.tsinghua.edu.cn/apache/maven/maven-3/3.8.1/binaries/apache-maven-3.8.1-bin.tar.gz
tar -xvf /usr/local/apache-maven-3.8.1-bin.tar.gz -C /usr/local
echo "export MAVEN_HOME=/usr/local/apache-maven-3.8.1" >> /etc/profile
echo "export PATH=\$PATH:\$MAVEN_HOME/bin" >> /etc/profile
source /etc/profile
mvn -version
