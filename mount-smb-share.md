# Mount SMB Share in Debian

```bash
sudo apt install cifs-utils
```

```bash
sudo mkdir /mnt/linux
```

Add the following content to `/root/.smbcredentials`:
```text
username=samba_username
password=samba_password
```

## Try to Mount with a One-Time Command
```bash
sudo mount -t cifs -o rw,credentials=/root/.smbcredentials,dir_mode=0775,file_mode=0775,uid=1000,gid=1000 //fileserver.example.co.uk/linux /mnt/linux
```

| Config                | Description                                                                       |
| --------------------- | --------------------------------------------------------------------------------- |
| `x-systemd.automount` | Automatically remounts the CIFS share in case the NAS went offline for some time. |
| `noatime`             | Access timestamps are not updated when a file/folder is read.                     |
## Make the Mount Permanent
Add the following line to `/etc/fstab`:
```text
//fileserver.example.co.uk/linux /mnt/linux-share cifs rw,x-systemd.automount,noatime,credentials=/root/.smbcredentials,dir_mode=0775,file_mode=0775,uid=1000,gid=1000 0 0
```
`systemd` will create mount units in `/run/systemd/generator/` from `/etc/fstab` on boot.

Reload mount unit
```shell
sudo systemctl daemon-reload
```
### Mount All Filesystems Mentioned in `fstab`

```shell
sudo mount -a
```
## Make a service wait for mount

Check service status & service file location

```shell
systemctl status <service-name>
```

Modify `/lib/systemd/system/<service-name>.service`, add:

```
[Unit]
RequiresMountsFor=/mnt/path
```
Reload systemd daemon

```shell
systemctl daemon-reload
```
### Refer
- https://www.reddit.com/r/systemd/comments/1bh2k5c/how_do_i_make_systemd_wait_until_an_nfs_volume_is/
- https://askubuntu.com/questions/876733/where-are-the-systemd-units-services-located-in-ubuntu