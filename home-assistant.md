# Home assistant

## Prepare image
Copy link of KVM file from HA website

In proxmox

    wget <ADDRESS>

Expand the compressed image

    unxz </path/to/file.qcow2.xz>

## Create VM

- OS:
  - Select 'Do not use any media'

- System:
  - Change 'machine' to 'q35'​【11 m】
  - Change BIOS to OVMF (UEFI)
  - Select the EFI storage (typically local-lvm/zfs)

- Disks:
  - Delete the SCSI drive and any other disks

Confirm and finish. Do not start the VM yet.

## Add the image to the VM

In console, use the following command to import the image from the host to the VM

    qm importdisk <VM ID> </path/to/file.qcow2> <EFI location>

For example,

    qm importdisk 205 /home/user/haos_ova-12.0.qcow2 local-lvm

In proxmox Web, select your HA VM
- Go to the 'Hardware' tab
- Select the 'Unused Disk' and click the 'Edit' button
- Check the 'Discard' box if you're using an SSD then click 'Add'
- Remove ROM/DVD device
- Select the 'Options' tab
- Select 'Boot Order' and hit 'Edit'
- Check the newly created drive (likely scsi0) and move is to the top

Finish Up
- Start the VM
- When `proxmox` logo showup, hit ESC, disable `secure boot`. Restart
- Check the shell of the VM. If it booted up correctly, you should be greeted with the link to access the Web UI.
- Navigate to <VM IP>:8123

Done. Everything should be up and running now.