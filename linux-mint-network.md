# Linux Mint network

## Setup static ip
Linux Mint use `netplan` to manage network interface

Find current interface setting
```
ls -lah /etc/netplan/
```
Modify  interface setting
```yaml
network:
  version: 2
  ethernets:
    eth0:
      dhcp4: false
      dhcp6: false
      addresses:
        - 192.168.0.51/24
      routes:
        - to: default
          via: 192.168.0.1
      nameservers:
        addresses: [192.168.0.1]
```
```
`netplan` might show warning about permission of configuration file, we can run
```
sudo chmod 600 /etc/netplan/your_config_file.yaml
```

Apply
```
sudo netplan apply
```
Check with `ifconfig enp2s0` to make sure it worked