# Debian

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
## List users
```
cat /etc/passwd
```
## List group
```
cat /etc/group
```

## Setup static ip

Finding your network interfaces name
```
ip -c link show
```
Show info
```
ip -c addr show enp0s5
```

Config
```
sudo vi /etc/network/interfaces
```
```
# The loopback network interface
auto lo
iface lo inet loopback

# The primary network interface
auto enp0s5
iface enp0s5  inet static
 address 192.168.2.236
 netmask 255.255.255.0
 gateway 192.168.2.254
 dns-domain sweet.home
 dns-nameservers 192.168.2.254 1.1.1.1 8.8.8.8
```
```
sudo systemctl restart networking.service
```

Perform traceroute using specific internet interface

    traceroute -i eth0 google.com

## Apt
Find package dependencies

    apt-cache depends <package>

Find package dependent

    apt-cache rdepends <package>

# Tools
|Name|Description|
|---|---|
|btop|Resource monitor that shows usage and stats for processor, memory, disks, network and processes|
|Nvtop|Task monitor for GPUs and accelerators|