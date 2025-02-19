# Debian post install

## Upgrade packages
```
apt update && apt upgrade -y
```
## Install basic essential packages
```
apt install -y sudo curl vim
```
## Change timezone
Check current time, timezone
```
date
timedatectl
cat /etc/localtime
```
List all available time zones
```
timedatectl list-timezones
```
Set time zone
```
sudo timedatectl set-timezone Asia/Tokyo
```
## Create user

Refer [[debian-common#Add user]]