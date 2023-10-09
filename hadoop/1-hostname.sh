read -p "请输入主机名: " hostname
hostnamectl set-hostname $hostname
echo "主机名已设置为: $hostname"
bash
