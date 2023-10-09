# 关闭SELinux
sed -i 's/SELINUX=enforcing/SELINUX=disabled/g' /etc/selinux/config
echo "SELinux已关闭，请重启系统使其生效"
reboot
