# Proxmox passing device in LXC

## Option 1: Mount device

Check device information

```shell
ls -lah /dev/net/
total 0
drwxr-xr-x  2 root root      60 Feb 22 10:53 .
drwxr-xr-x 21 root root    5.3K Feb 22 10:53 ..
crw-rw-rw-  1 root root 10, 200 Feb 22 10:53 tun
```
As we can see, `/dev/net/tun` identified by major number 10 and minor number 200

Modify `/etc/pve/lxc/<lxc-id>.conf`

```
lxc.cgroup2.devices.allow: c 10:200 rwm
lxc.mount.entry: /dev/net dev/net none bind,create=dir
```
In above example:
- The first line instruct the kernel to allow access to specific device
    1. **`c`** indicates that this is a character device (as opposed to a block device, which would start with `b`).
    2. **`10:200`** represents the major and minor numbers of the device.
    3. **`rwm`** : This specifies the permissions for the device:
        - **`r`** means read access
        - **`w`** means write access
        - **`m`** means memory map access
- The second line specifies that a container should be allowed to mount a specific directory inside its root file system. In this example, it is specifying that the `/dev/net` directory should be mounted as `/dev/net` in the container's root file system. This allows the container to access the network devices and interfaces on the host system.

You can also mount specific file instead of directory
```
lxc.mount.entry = /dev/net/tun dev/net/tun none bind,create=file
```

## Option 2: New way

```
dev0: /dev/dri/card0,gid=44,uid=0
```
- `gid` (optional): specifies the group ID of the user who owns the device inside container.
- `uid` (optional): specifies the user ID of the user who owns the device inside container

## Reference
[Proxmox-share-GPU-multiple-LXC](Proxmox-share-GPU-multiple-LXC.md)
https://wiki.debian.org/LXC#Bind_mounts_inside_the_container