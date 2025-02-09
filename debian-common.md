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

Remove package

    apt remove <package-name>

Remove package and its configuration

    apt purge <package-name>

To uninstall package and its dependencies

    apt autoremove <package-name>

To uninstall package and its dependencies and its configuration

    apt autoremove --purge <package-name>
    apt purge --autoremove <package-name>
## Get size of all files/directories in current directory

    du -h --max-depth=1

## Read booting log
The dmesg command allows you to review messages stored in the Linux ring buffer, providing insights into hardware errors and startup issues

    dmesg -T

## Read `systemd` service log

    sudo journalctl -u <unit-name> -n 100
    sudo journalctl --since="25-01-17 10:00:00"

## Config log rotate
Add `/etc/logrotate.d/traefik` file

    compress
    /var/log/traefik/*.log {
        size 20M
        daily
        rotate 14
        missingok
        notifempty postrotate
        docker kill --signal="USR1" traefik # adjust this line to your traefik container name
        endscript
    }

Confirm

    sudo logrotate -d /etc/logrotate.d/traefik

## Other
Copy without symbolic links

    cp -rfL /source/* /destination/

Find file by name recursively

    find . -iname "foo*"

Unzip

    unzip file.zip -d <directory>
## Tools
|Name|Description|
|---|---|
|btop|Resource monitor that shows usage and stats for processor, memory, disks, network and processes|
|nvtop|Task monitor for GPUs and accelerators|

## Send log to remote server using Syslog
Install `rsyslog`

    apt update && apt install rsyslog

Setting `rfc5424` log format for forwarding. Modify `/etc/rsyslog.conf`

    $ActionForwardDefaultTemplate RSYSLOG_SyslogProtocol23Format

Add forwarding config

     echo '*.* @@remote-host:port' > /etc/rsyslog.d/promtail.conf

Note: `@` for UDP, `@@` for TCP protocol

Restart `rsyslog`

    sudo systemctl restart syslog

## Send log to remote server using Journal

### On Server side
Install

    sudo apt install systemd-journal-remote

Modify `/lib/systemd/system/systemd-journal-remote.service`
- to use `http`, change `--listen-https=-3` to `--listen-http=-3`
- Change `LogsDirectory` if needed

Modify `/lib/systemd/system/systemd-journal-remote.socket`
- Change `ListenStream` (port number) if needed

Enable & start service

    sudo systemctl enable --now systemd-journal-remote.service

### On client side
Install

    sudo apt install systemd-journal-remote

Modify `/etc/systemd/journal-upload.conf`

    URL=http://<host>:19532

Enable & start service

    sudo systemctl enable --now systemd-journal-upload.service 