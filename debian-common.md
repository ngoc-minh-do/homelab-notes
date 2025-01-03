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