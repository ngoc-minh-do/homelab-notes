# Share GPU between multiple LXC
## Unprivileged LXC containers
https://pve.proxmox.com/wiki/Unprivileged_LXC_containers

These kind of containers use a new kernel feature called user namespaces. All of the UIDs (user id) and GIDs (group id) are mapped to a different number range than on the host machine, usually root (uid 0) became uid 100000, 1 will be 100001 and so on
## Find Group Numbers. Focus on video(44), render(104) groups
```
cat /etc/group
```
## Find Device info.
```
ls -l /dev/dri
```
Focus on GPU device, something like `renderD128`.
We will see that `renderD128` has `226 128` (major device, minor device number), and so on.

If there are multiple GPU, use below command to check GPU mapping

    ls -l /sys/class/drm/renderD*/device/driver
    ls -l /dev/dri/by-path

Run bellow command to check what GPU is in system
```
lspci | grep VGA
```
## Edit /etc/pve/lxc/<VMID>.conf, add bellow lines
```
dev0: /dev/dri/card0,gid=44,uid=0
dev1: /dev/dri/renderD128,gid=105,uid=0
```
`44` is GID of `video` group, `105` is GID of `render` group in LXC, change it if needed.
Reboot LXC and check group name in LXC, make sure it same as host

    ls -l /dev/dri
## Install NVIDIA GPU in LXC
After install NVIDIA GPU on Host, additional devices need to be mapped in the container.

List all NVIDIA GPU devices, determine major device, minor device number

    ls -al /dev/nvidia*

Then add below line to `/etc/pve/lxc/*.conf` to share those devices.
**NOTE**: Modify GID corresponding to those devices

    lxc.cgroup2.devices.allow: c 195:* rwm
    lxc.cgroup2.devices.allow: c 235:* rwm
    lxc.cgroup2.devices.allow: c 510:* rwm
    lxc.mount.entry: /dev/nvidia0 dev/nvidia0 none bind,optional,create=file
    lxc.mount.entry: /dev/nvidiactl dev/nvidiactl none bind,optional,create=file
    lxc.mount.entry: /dev/nvidia-modeset dev/nvidia-modeset none bind,optional,create=file
    lxc.mount.entry: /dev/nvidia-uvm dev/nvidia-uvm none bind,optional,create=file
    lxc.mount.entry: /dev/nvidia-uvm-tools dev/nvidia-uvm-tools none bind,optional,create=file
    lxc.mount.entry: /dev/nvidia-caps/nvidia-cap1 dev/nvidia-caps/nvidia-cap1 none bind,optional,create=file
    lxc.mount.entry: /dev/nvidia-caps/nvidia-cap2 dev/nvidia-caps/nvidia-cap2 none bind,optional,create=file

With this all setup and the container rebooted, the same installer for the Nvidia drivers on the Proxmox host will need to be run on the container. To get the installer into the container, the following command can be used. I have put this in the root user directory of the container.

    sudo pct push <VMID> ./NVIDIA-Linux-x86_64-550.142.run /tmp/NVIDIA-Linux-x86_64-550.142.run
All that is left to do is install the drivers again without the kernel modules because the LXC container shares the host's kernel.

    sudo chmod +x ./NVIDIA-Linux-x86_64-550.142.run
    sudo ./NVIDIA-Linux-x86_64-550.142.run --no-kernel-module
Reboot

    sudo reboot
Confirm Nvidia drivers should now be installed

    sudo nvidia-smi

# Ref
- https://forum.proxmox.com/threads/solved-lxc-unable-to-access-gpu-by-id-mapping-error.145086/
- https://yomis.blog/nvidia-gpu-in-proxmox-lxc/