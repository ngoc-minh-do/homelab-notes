# NAS share on LXC
## Unprivileged LXC containers

These kind of containers use a new kernel feature called user namespaces. All of the UIDs (user id) and GIDs (group id) are mapped to a different number range than on the host machine, usually root (uid 0) became uid 100000, 1 will be 100001 and so on

https://pve.proxmox.com/wiki/Unprivileged_LXC_containers
## On Proxmox Host

Create a folder to mount the NAS
```
mkdir -p /mnt/linux
```

Add NAS CIFS share to `/etc/fstab`
```
//<nas-ip-address>/linux /mnt/linux cifs _netdev,x-systemd.automount,noatime,credentials=/root/.smbcredentials,uid=101000,gid=101000,dir_mode=0770,file_mode=0770 0 0
```

| Config                         | Description                                                                                        |
| ------------------------------ | -------------------------------------------------------------------------------------------------- |
| `_netdev`                      | Forces systemd to consider the mount unit a network mount.                                         |
| `x-systemd.automount`          | Automatically remounts the CIFS share in case the NAS went offline for some time.                  |
| `noatime`                      | Access timestamps are not updated when a file/folder is read.                                      |
| `uid=101000,gid=101000`        | map to user in LXC container                                                                       |
| `dir_mode=0770,file_mode=0770` | Only that uid/gid will have rwx access to the share. (PVE root user always has rwx to everything.) |
Reload mount unit
```sh
sudo systemctl daemon-reload
```

Mount the NAS to the Proxmox Host
```sh
sudo mount -a
```

Add Bind Mount of the Share to the LXC Config
```
mp0: /mnt/linux,mp=/mnt/linux
```

You can also mount it in the LXC with read-only (ro) permissions.
```
mp0: /mnt/linux,mp=/mnt/linux,ro=1
```
## Reference
[mount-smb-share](mount-smb-share.md)