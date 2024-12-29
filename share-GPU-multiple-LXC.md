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
## Find Device Numbers(major device, minor device number). Focus on GPU device, something like `renderD128`
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

## NVIDIA GPU
https://yomis.blog/nvidia-gpu-in-proxmox-lxc/

After install NVIDIA GPU on Host, additional devices need to be mapped in the container.

List all NVIDIA GPU devices, determine major device, minor device number

    ls -al /dev/nvidia*

Then add below line to `/etc/pve/lxc/*.conf` to share those devices.
**NOTE**: Modify GID corresponding to those devices

    lxc.cgroup2.devices.allow: c 195:0 rwm
    lxc.cgroup2.devices.allow: c 195:255 rwm
    lxc.cgroup2.devices.allow: c 510:0 rwm
    lxc.cgroup2.devices.allow: c 510:1 rwm
    lxc.cgroup2.devices.allow: c 235:1 rwm
    lxc.cgroup2.devices.allow: c 235:2 rwm
    lxc.mount.entry: /dev/nvidia0 dev/nvidia0 none bind,optional,create=file
    lxc.mount.entry: /dev/nvidiactl dev/nvidiactl none bind,optional,create=file
    lxc.mount.entry: /dev/nvidia-uvm dev/nvidia-uvm none bind,optional,create=file
    lxc.mount.entry: /dev/nvidia-uvm-tools dev/nvidia-uvm-tools none bind,optional,create=file
    lxc.mount.entry: /dev/nvidia-caps/nvidia-cap1 dev/nvidia-caps/nvidia-cap1 none bind,optional,create=file
    lxc.mount.entry: /dev/nvidia-caps/nvidia-cap2 dev/nvidia-caps/nvidia-cap2 none bind,optional,create=file

**NOTE** `195:0` meaning "195" is the major device number, and "0" is the minor device number, uniquely identifying a particular device.

With this all setup and the container rebooted, the same installer for the Nvidia drivers on the Proxmox host will need to be run on the container. To get the installer into the container, the following command can be used. I have put this in the root user directory of the container.

    sudo pct push <VMID> /tmp/NVIDIA-Linux-x86_64-550.142.run /tmp/NVIDIA-Linux-x86_64-550.142.run
All that is left to do is install the drivers again without the kernel modules because they have already been installed. Look up what `cgroup` is for more details on how this works - the LXC container shares the host's kernel.

    sudo ./NVIDIA-Linux-x86_64-550.142.run --no-kernel-module
Et voila. After the driver installation is complete, `nvidia-smi` can be run once more to confirm that things have been installed as expected.