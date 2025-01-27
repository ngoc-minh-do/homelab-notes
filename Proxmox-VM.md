# Proxmox VM

## Create VM

1. General

    Enter a Name for the VM

1. OS

    Select iso image

1. System

        Machine: q35
        Bios: OVMF (UEFI)

1. Disks

        Bus/Device: SCSI
        Disk size (GiB): Appropriate number
1. CPU

        Cores: 4
        Type: x86-64-v4

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