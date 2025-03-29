# Debian common command

## List users
```
cat /etc/passwd
```
## List group
```
cat /etc/group
```
## Add user
```
sudo adduser username
```
Next, you will be prompted to provide the user’s password. Once you have provided and confirmed the password, you will be required to provide additional information about the user, such as full name, room number, work phone, and home phone. Fill in the information where applicable, or hit ENTER to skip.

Add user to `sudo` group
```
usermod -aG sudo username
```
## Remove user
```
userdel -r username
```

`-r` is for delete user's home directory and mail spool

## Apt

Find package dependencies
```
apt-cache depends <package>
```

Find package dependent
```
apt-cache rdepends <package>
```

Remove package
```
apt remove <package-name>
```

Remove package and its configuration
```
apt purge <package-name>
```

To uninstall package and its dependencies
```
apt autoremove <package-name>
```

To uninstall package and its dependencies and its configuration
```
apt autoremove --purge <package-name>
apt purge --autoremove <package-name>
```

## Check disk usage/remaining space
```shell
df -hT
```

## Get size of all files/directories in current directory
```
du -h --max-depth=1
```
## Read booting log
The dmesg command allows you to review messages stored in the Linux ring buffer, providing insights into hardware errors and startup issues
```
dmesg -T
```
## Read `systemd` service log
```
sudo journalctl -u <unit-name> -n 100
sudo journalctl --since="25-01-17 10:00:00"
```
## Config log rotate
Add `/etc/logrotate.d/traefik` file
```
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
```

Confirm
```
sudo logrotate -d /etc/logrotate.d/traefik
```
## `top` command

- Arrow keys & page up/down: Navigate through the displayed list in the Task area.
- q: Finish the top with the q-key.
- shift + p: Sort the processes by CPU usage.
- shift + m: Sort the processes by memory (%MEM) usage.
- shift + t: Sort the processes by running-time.
- shift + n: Sort the processes by process ID.
- t: Changes the display of the CPU usage in the summary section.
- m: Changes the display of memory usage in the summary section.
- shift + r: Sort the processes in ascending order instead of descending (default).
- c: By pressing c, the 'Command' column shows the entire path from which the processes were started.
- shift + v: Shows the parent / child process hierarchy.
- k: Prompts for a process ID and closes the specified process. By default, SIGTERM is used for a graceful shutdown of the process. For a forced shutdown, you use SIGKILL.
## Other
Copy without symbolic links
```
cp -rfL /source/* /destination/
```

Find file by name recursively
```
find . -iname "foo*"
```

Unzip
```
unzip file.zip -d <directory>
```
## Tools
| Name  | Description                                                                                     |
| ----- | ----------------------------------------------------------------------------------------------- |
| btop  | Resource monitor that shows usage and stats for processor, memory, disks, network and processes |
| nvtop | Task monitor for GPUs and accelerators                                                          |