# Proxmox VM

## Create VM

1. General

    Enter a Name for the VM

1. OS

    Select iso image

1. System

        Machine: q35 (Secure boot)
        Bios: OVMF (UEFI)

1. Disks

        Bus/Device: VirtIO Block

    According to same test, `VirtIO Block` faster than `SCSI`.

    Refer: https://forum.proxmox.com/threads/virtio-vs-scsi.52893/

1. CPU

        Cores: 4
        Type: x86-64-v4

1. Memory

        Memory (MiB): Appropriate number

1. Network

    Appropriate Setting