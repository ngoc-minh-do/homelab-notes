# Proxmox VM

## Create VM

1. General

    Enter a Name for the VM

1. OS

        Select iso image
        Type: Linux or Windows
        Version: Pick the latest
    For Windows:

        Add additional drive for VirtIO drivers: Check
        And point to virtio-win iso file
1. System

        Machine: q35
        Bios: OVMF (UEFI)
        SCSI Controller: VirtIO SCSI single
        EFI Storage: specific storage
        Qemu Agent: Check
    For Windows:

        Add TPM: Check
        TPM Storage: specific storage

1. Disks

        Bus/Device: SCSI
        Disk size (GiB): Appropriate number
        Discard: Check
        IO Thread: Check
        SSD emulation: Check
1. CPU

        Cores: 4
        Type: `x86-64-v4` or `host`

1. Memory

        Memory (MiB): Appropriate number

1. Network

    Appropriate Setting

1. Confirm and Start VM
1. (Optional) Disable secure boot

        Hit `Esc` while the boot splash screen is visible
        Select `Device Manager`
        Select `Secure Boot Configuration`
        Uncheck `Attempt Secure Boot`
        Select Continue
        Select Restart

## Post install (Windows)
- Install the **Guest Agent** from the VirtIO Win ISO: `guest-agent\qemu-ga-x86_64.msi`.
- Install the driver from the VirtIO Win ISO: `virtio-win-gt-x64.msi`. Check for any missing drivers. If found, select **Update Driver**, then specify the VirtIO Win ISO location
- (Optional) Install `virtio-win-guest-tools.exe` if you want all at one (**Drivers**, **Guest Agent**, **SPICE Agent**...)
- Activate Windows.
- Update Windows.
- Enable **Remote Desktop**: *Settings > System > Remote Desktop*. (If using a Microsoft account, login with a password is required.)
- Configure a static IP.

## Ref
- https://pve.proxmox.com/wiki/Windows_10_guest_best_practices
- https://pve.proxmox.com/wiki/Install_Proxmox_VE_on_Debian_12_Bookworm
- https://docs.redhat.com/en/documentation/red_hat_virtualization/4.4/html/virtual_machine_management_guide/installing_guest_agents_and_drivers_windows
- [Qemu-guest-agent - Proxmox VE](https://pve.proxmox.com/wiki/Qemu-guest-agent)