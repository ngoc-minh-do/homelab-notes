# Passthrough GPU on Proxmox

## Confirm target GPU is in a dedicated IOMMU group (IOMMU isolation)
```sh
pvesh get /nodes/<proxmox-nodename>/hardware/pci --pci-class-blacklist ""
```
## Determine which Bootloader is Used (`GRUB` or `systemd-boot`)
```sh
efibootmgr -v
proxmox-boot-tool status
```
## Enable IOMMU for GRUB Bootloader

Modify `/etc/default/grub`, append bellow value to `GRUB_CMDLINE_LINUX_DEFAULT` variable
```
 intel_iommu=on iommu=pt
```
Then run
```sh
update-grub
```
## Kernel Modules
Modify `/etc/modules`, append bellow line
```
vfio
vfio_iommu_type1
vfio_pci
```
## Ensure that the `vfio-pci` module is loaded first, using `softdep`
Run
```sh
lspci -nn | grep 'NVIDIA'
```
It should be something like this
```
0000:65:00.0 VGA compatible controller [0300]: NVIDIA Corporation GA106 [GeForce RTX 3060 Lite Hash Rate] [10de:2504] (rev a1)
0000:65:00.1 Audio device [0403]: NVIDIA Corporation GA106 High Definition Audio Controller [10de:228e] (rev a1)
```
Then the pair `<vendor id:device id>` of target GPU will be
```
10de:2504 (for VGA)
10de:228e (for Audio)
```
Create a configuration file `/etc/modprobe.d/vfio.conf` to specify the PCI IDs to be isolated, also define a loading order for module
```
options vfio-pci ids=10de:2504,10de:228e disable_vga=1
# For Nvidia
softdep nvidiafb pre: vfio-pci
softdep nouveau pre: vfio-pci
softdep nvidia_drm pre: vfio-pci
softdep nvidia pre: vfio-pci
softdep snd_hda_intel pre: vfio-pci
```
**NOTE**:
- To get the list of modules need to be include in above config, run `lspci -nnk | grep -A 3 'NVIDIA'` and check `Kernel modules:` line

## Refresh your initramfs
```sh
update-initramfs -u -k all
```
## Finish Configuration
Finally reboot to bring the changes into effect and check that it is indeed enabled.

Confirm IOMMU:
```sh
dmesg | grep -E "DMAR|IOMMU"
```

```
DMAR: IOMMU enabled
DMAR: Intel(R) Virtualization Technology for Directed I/O
```
Confirm Remapping:
```sh
dmesg | grep 'remapping'
```

```
DMAR-IR: Queued invalidation will be enabled to support x2apic and Intr-remapping.
DMAR-IR: Enabled IRQ remapping in x2apic mode
```
To check if the VFIO modules are being loaded
```sh
lsmod | grep -i vfio
```
Confirm current `Kernel driver in use`. Should be `vfio-pci` or the line is missing entirely
```sh
lspci -nnk | grep -A 3 'NVIDIA'
lspci -v
```
## Setting VM

Add GPU using raw device 
```
All Functions: Check
Primary GPU: Check
PCIe: Check
```
## Ref
- https://pve.proxmox.com/pve-docs/pve-admin-guide.html#sysboot_determine_bootloader_used
- https://pve.proxmox.com/pve-docs/pve-admin-guide.html#qm_pci_passthrough
- https://pve.proxmox.com/wiki/PCI_Passthrough#Verifying_IOMMU_parameters
- https://pve.proxmox.com/pve-docs/pve-admin-guide.html#qm_pci_passthrough_vm_config
- https://forum.proxmox.com/threads/pci-gpu-passthrough-on-proxmox-ve-8-installation-and-configuration.130218/