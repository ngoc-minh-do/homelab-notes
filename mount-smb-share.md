# Mount SMB share

```
sudo apt install cifs-utils
```
```
sudo mkdir /mnt/linux-share
```
```
sudo nano /root/.smbcredentials
username=samba_username
password=samba_password
```
Try to mount by 1 time command
```
sudo mount -t cifs -o rw,credentials=/root/.smbcredentials,dir_mode=0775,file_mode=0775,uid=1000,gid=1000 //fileserver.example.co.uk/linux /mnt/linux-share
```
Make the mount permanent
```
sudo nano /etc/fstab
//fileserver.example.co.uk/linux /mnt/linux-share cifs rw,x-systemd.automount,noatime,credentials=/root/.smbcredentials,dir_mode=0775,file_mode=0775,uid=1000,gid=1000 0 0
```
Mount all filesystems mentioned in fstab
```
mount -a
```