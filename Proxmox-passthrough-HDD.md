# Passthrough HDD on Proxmox

## Check SMART data

```
smartctl --all /dev/sda
```
## Check speed
Maximum throughput with a much higher blocksize, simulating video downloads
```
fio --ioengine=libaio --direct=1 --sync=1 --rw=read --bs=1M --numjobs=1 --iodepth=1 --runtime=60 --time_based --name seq_read --filename=/dev/sda
```
4K performance
```
fio --ioengine=libaio --direct=1 --sync=1 --rw=read --bs=4K --numjobs=1 --iodepth=1 --runtime=60 --time_based --name seq_read --filename=/dev/sda
```
## Pass through HDD
```
ls -l /dev/disk/by-id/
lsblk -o +MODEL,SERIAL,WWN
qm set 100 -scsi3 /dev/disk/by-id/ata-ST2000DM006-2DM164_Z5610A2V,serial=Z5610A2V
cat /etc/pve/qemu-server/100.conf
```
**NOTE**:
Also add `,backup=0` if you want to tell proxmox these volume out of proxmox's backup job