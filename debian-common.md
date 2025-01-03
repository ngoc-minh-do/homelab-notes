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

## Add user

    sudo adduser alex
Next, you will be prompted to provide the user’s password. Once you have provided and confirmed the password, you will be required to provide additional information about the user, such as full name, room number, work phone, and home phone. Fill in the information where applicable, or hit ENTER to skip.

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