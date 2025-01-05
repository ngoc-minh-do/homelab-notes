# NAS share on LXC
Solution:
```
You simply mount the CIFS share to the UID that belongs to the unprivileged LXC root user, which by default is always uid=100000.
But instead of also mounting it to the GID of the LXC root user, your are going to create a group in your LXC called lxc_cifs_shares with a gid=10000 which refers to gid=110000 on the PVE host.
PVE host (UID=100000/GID=110000) <--> unprivileged LXC (UID=0/GID=10000)
```
## On LXC Create User Group
```
groupadd -g 10000 lxc_shares
```
**NOTE**: GID 10000 in LXC will refer to GID 110000 in PVE Host

## Optional: Add Other Users to Group (e.g., Jellyfin, Plex)
```
usermod -aG lxc_shares USERNAME
```
- `-a`: append
- `-G`: list of groups
## On Proxmox Host
Create a folder to mount the NAS
```
mkdir -p /mnt/lxc_shares/nas_rwx
```

## Add NAS CIFS share to /etc/fstab
Replace //NAS-IP-ADDRESS with your NAS IP
Replace Username and Passwords
```
//NAS-IP-ADDRESS/nas/ /mnt/lxc_shares/nas_rwx cifs _netdev,x-systemd.automount,noatime,credentials=/root/.smbcredentials,uid=100000,gid=110000,dir_mode=0770,file_mode=0770 0 0

```
|Config|Description|
|---|---|
|`_netdev` | Forces systemd to consider the mount unit a network mount.|
|`x-systemd.automount` | Automatically remounts the CIFS share in case the NAS went offline for some time.|
|`noatime` | Access timestamps are not updated when a file/folder is read.|
|`uid=100000,gid=110000 | See `Solution` part|
|`dir_mode=0770,file_mode=0770` | Only that uid/gid will have rwx access to the share. (PVE root user always has rwx to everything.)|

## Mount the NAS to the Proxmox Host
```
mount /mnt/lxc_shares/nas_rwx
```

## Add Bind Mount of the Share to the LXC Config
You can mount it in the LXC with read+write+execute (rwx) permissions in `/etc/pve/lxc/LXC_ID.conf`

    mp0: /mnt/lxc_shares/nas_rwx/,mp=/mnt/nas

You can also mount it in the LXC with read-only (ro) permissions.

    mp0: /mnt/lxc_shares/nas_rwx/,mp=/mnt/nas,ro=1
