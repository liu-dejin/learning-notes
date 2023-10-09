tar -zxvf jdk-8u271-linux-x64.tar.gz -C /opt/
echo "export JAVA_HOME=/opt/jdk1.8.0_271" >> /etc/profile
echo "export PATH=\$PATH:\$JAVA_HOME/bin" >> /etc/profile
source /etc/profile
echo "JDK环境已部署"
