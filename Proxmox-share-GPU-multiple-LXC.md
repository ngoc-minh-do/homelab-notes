# Share GPU between multiple LXC
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
```
ls -l /sys/class/drm/renderD*/device/driver
ls -l /dev/dri/by-path
```

Run bellow command to check what GPU is in system
```
lspci | grep VGA
```
## Edit `/etc/pve/lxc/<VMID>.conf`, add bellow lines
```
dev0: /dev/dri/card0,gid=44,uid=0
dev1: /dev/dri/card1,gid=44,uid=0
dev2: /dev/dri/renderD128,gid=104,uid=0
```
`44` is GID of `video` group, `104` is GID of `render` group in LXC, change it if needed.
Reboot LXC and check group name in LXC, make sure it same as host
```
ls -l /dev/dri
```

*For more information, refer: [Proxmox-passing-device-in-LXC](Proxmox-passing-device-in-LXC.md)*
## For NVIDIA GPU in LXC

### Passing Nvidia device node to LXC container

#### Method 1:
Add below line to `/etc/pve/lxc/*.conf` to share those devices.
```
dev3: /dev/nvidia0
dev4: /dev/nvidiactl
dev5: /dev/nvidia-modeset
dev6: /dev/nvidia-uvm
dev7: /dev/nvidia-uvm-tools
dev8: /dev/nvidia-caps/nvidia-cap1
dev9: /dev/nvidia-caps/nvidia-cap2
```

#### Method 2 (old way):
List all NVIDIA GPU devices, determine major device, minor device number
```
ls -al /dev/nvidia*
```

Change major device number according to your and add below line to `/etc/pve/lxc/*.conf` to share those devices.
```
lxc.cgroup2.devices.allow: c 195:* rwm
lxc.cgroup2.devices.allow: c 234:* rwm
lxc.cgroup2.devices.allow: c 237:* rwm
lxc.mount.entry: /dev/nvidia0 dev/nvidia0 none bind,optional,create=file
lxc.mount.entry: /dev/nvidiactl dev/nvidiactl none bind,optional,create=file
lxc.mount.entry: /dev/nvidia-modeset dev/nvidia-modeset none bind,optional,create=file
lxc.mount.entry: /dev/nvidia-uvm dev/nvidia-uvm none bind,optional,create=file
lxc.mount.entry: /dev/nvidia-uvm-tools dev/nvidia-uvm-tools none bind,optional,create=file
lxc.mount.entry: /dev/nvidia-caps dev/nvidia-caps none bind,optional,create=dir
```

*For more information, refer: [Proxmox-passing-device-in-LXC](Proxmox-passing-device-in-LXC.md)*

### Install Nvidia driver in LXC Container

With this all setup and the container rebooted, the same installer for the Nvidia drivers on the Proxmox host will need to be run on the container. To get the installer into the container, the following command can be used. I have put this in the root user directory of the container.
```
sudo pct push <VMID> ./NVIDIA-Linux-x86_64-550.142.run /tmp/NVIDIA-Linux-x86_64-550.142.run
```
All that is left to do is install the drivers again without the kernel modules because the LXC container shares the host's kernel.
```
sudo chmod +x /tmp/NVIDIA-Linux-x86_64-550.142.run
sudo /tmp/NVIDIA-Linux-x86_64-550.142.run --no-kernel-module
```
On GUI
- When `Can't find X library path`, ignore and select OK
- When asked `Install NVIDIA's 32-bit compatibility libraries`, select `NO`
- When asked for `nvidia-xconfig` utility and backup pre-existing X configuration, select `NO` (since this is headless system)
Reboot
```
sudo reboot
```
Confirm Nvidia drivers should now be installed
```
sudo nvidia-smi
```

## Reference
- https://forum.proxmox.com/threads/solved-lxc-unable-to-access-gpu-by-id-mapping-error.145086/
- https://yomis.blog/nvidia-gpu-in-proxmox-lxc/
- https://www.reddit.com/r/Proxmox/comments/18xxcbg/cgroup2_how_to_deal_with_device_numbers_changing/