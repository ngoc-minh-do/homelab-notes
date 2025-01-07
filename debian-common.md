# Debian common command

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

    sudo adduser username
Next, you will be prompted to provide the user’s password. Once you have provided and confirmed the password, you will be required to provide additional information about the user, such as full name, room number, work phone, and home phone. Fill in the information where applicable, or hit ENTER to skip.

Add user to `sudo` group

    usermod -aG sudo username

## Remove user

    userdel -r username

`-r` is for delete user's home directory and mail spool
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