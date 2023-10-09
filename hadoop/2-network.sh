# 配置静态IP地址和DNS服务器地址
read -p "请输入IP地址: " ip_address
read -p "请输入子网掩码: " subnet_mask
cat <<EOL > /etc/sysconfig/network-scripts/ifcfg-ens33
TYPE=Ethernet
BOOTPROTO=none
DEFROUTE=yes
IPADDR=$ip_address
NETMASK=$subnet_mask
GATEWAY=your_gateway_ip
DNS1=114.114.114.114
ONBOOT=yes
NAME=ens33
DEVICE=ens33
EOL
systemctl restart network
echo "静态IP地址已配置为: $ip_address"
echo "DNS服务器地址已配置为: 114.114.114.114"


