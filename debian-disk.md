# Debian disk

## 📊 Check Disk Usage and Partition Info

Use the following commands to view disk space, partitions, and layouts:
```sh
df -hT        # View disk usage with filesystem types 
lsblk         # List block devices 
fdisk -lu     # Detailed partition table (MBR) 
sfdisk -l     # Alternative partition listing
```

---
## 🔁 Swap Partition Management

### ✅ Enable a Swap Partition

1. **Create the Swap Partition** using `parted`:
```
parted > unit s              # Use sectors for units 
> print free          # Show available space 
> mkpart primary swap-partition <start-sector>s 100%
```

2. **Initialize the Swap Area**:
```sh
swapon /dev/sdaX
```

3. **Enable the Swap**:
```sh
swapon /dev/sdaX
```

4. **Verify Swap Status**:
```
swapon --show
```

5. **Make Swap Permanent**:

- Get the UUID of the swap partition:
```
blkid
```
    
- Edit `/etc/fstab` and add:
```
`UUID=<swap-partition-uuid> none swap sw 0 0`
```

---
### 🚫 Disable a Swap Partition

1. **Turn Off the Swap**:
```
swapoff /dev/sdX
```

2. **Verify**:
```
swapon --show
```

3. **Delete the Partition**:
```
parted
> print free
> rm <partition-number>`
```

---
## ⬆️ Extend a Partition

1. **Resize with `parted`**:
```
parted 
> print free 
> resizepart <partition-number> 100%
```


2. Resize the filesystem inside the partition
```
resize2fs /dev/sdX
```

3. Verify
```
df -h
```
## Reference
- [Resize disks - Proxmox VE](https://pve.proxmox.com/wiki/Resize_disks)