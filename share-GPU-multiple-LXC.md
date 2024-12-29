# Share GPU between multiple LXC
## Unprivileged LXC containers
https://pve.proxmox.com/wiki/Unprivileged_LXC_containers

These kind of containers use a new kernel feature called user namespaces. All of the UIDs (user id) and GIDs (group id) are mapped to a different number range than on the host machine, usually root (uid 0) became uid 100000, 1 will be 100001 and so on
## Find Group Numbers. Focus on video(44), render(104) groups
```
cat /etc/group
```
## Add Root to Groups
```
usermod -aG render,video root
```
## Add Group Numbers Values to subgid
This allows `root` to map thoses groups to a new GID later
```
vi /etc/subgid
```
Paste at the bottom
```
root:44:1
root:104:1
```
## Find Device Numbers. Focus on GPU device, something like `renderD128`
```
ls -l /dev/dri
```
We will see that GID 128 is assigned to `renderD128`, and so on.

Run bellow command to check what GPU is in system
```
lspci | grep VGA
```
## Create CT Using Wizard. Edit .conf In /etc/pve/lxc/, add bellow lines
```
lxc.cgroup2.devices.allow: c 226:0 rwm
lxc.cgroup2.devices.allow: c 226:128 rwm
lxc.mount.entry: /dev/dri/renderD128 dev/dri/renderD128 none bind,optional,create=file
lxc.idmap: u 0 100000 65536
lxc.idmap: g 0 100000 44
lxc.idmap: g 44 44 1
lxc.idmap: g 45 100045 62
lxc.idmap: g 107 104 1
lxc.idmap: g 108 100108 65428
```
**NOTE**: replace `128` to other number if GPU ID is different

|Config|Description|
|---|---|
|lxc.idmap: u 0 100000 65536|# map UIDs 0-65536 (LXC namespace) to 100000-165535 (host namespace)|
|lxc.idmap: g 0 100000 44|# map GIDs 0-43 (LXC namspace) to 100000-100043 (host namespace)|
|lxc.idmap: g 44 44 1|# map GID 44 to be the same in both namespaces|
|lxc.idmap: g 45 100045 62|# map GIDs 45-106 (LXC namspace) to 100045-100106 (host namespace)<br /># 106 is the group before the render group (107) in LXC container<br /># 62 = 107 (render group in LXC) - 45 (start group for this mapping)|
|lxc.idmap: g 107 103 1|# map GID 107 (render in LXC) to 103 (render on the host)|
|Lxc.idmap: g 108 100108 65428|# map GIDs 108-65536 (LXC namspace) to 100108-165536 (host namespace)<br /># 108 is the group after the render group (107) in the LXC container<br /># 65428 = 65536 (max gid) - 108 (start group for this mapping)|