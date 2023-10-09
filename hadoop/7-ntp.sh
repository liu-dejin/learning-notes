# ntp服务
yum install -y ntp 
rm -f /etc/localtime;sudo ln -s /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
ntpdate -u ntp.aliyun.com
systemctl start ntpd
systemctl enable ntpd
