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

### Try to Mount with a One-Time Command
```bash
sudo mount -t cifs -o rw,credentials=/root/.smbcredentials,dir_mode=0775,file_mode=0775,uid=1000,gid=1000 //fileserver.example.co.uk/linux /mnt/linux
```
|Config|Description|
|---|---|
|`x-systemd.automount` | Automatically remounts the CIFS share in case the NAS went offline for some time.|
|`noatime` | Access timestamps are not updated when a file/folder is read.|

### Make the Mount Permanent
Add the following line to `/etc/fstab`:
```text
//fileserver.example.co.uk/linux /mnt/linux-share cifs rw,x-systemd.automount,noatime,credentials=/root/.smbcredentials,dir_mode=0775,file_mode=0775,uid=1000,gid=1000 0 0
```

### Mount All Filesystems Mentioned in `fstab`
```bash
sudo mount -a
