# Network

## Setup static ip

Finding your network interfaces name
```
ip -c link show
ip addr
```
Show info
```
ip -c addr show enp0s5
```

Config
```
sudo vi /etc/network/interfaces
```
```
# The loopback network interface
auto lo
iface lo inet loopback

# The primary network interface
auto enp0s5
iface enp0s5  inet static
 address 192.168.2.236
 netmask 255.255.255.0
 gateway 192.168.2.254
 dns-domain sweet.home
 dns-nameservers 192.168.2.254 1.1.1.1 8.8.8.8
```
```
sudo systemctl restart networking.service
```

## Route
  
Perform traceroute using specific internet interface

    traceroute -i eth0 google.com
Trace route to a service (Windows)

    tracert 8.8.8.8
## Scan Local network

Scan all ip in local network

    nmap -sn 192.168.0.*

Scan all ip and port

    nmap 192.168.0.*

Flags have the following meanings:
- -vv (Increase verbosity)
- -n (No DNS resolution. This speeds up our scan!)
- -sn (No port scan)
- -PE (Use ICMP echo request queries. This is what is displayed in the output above)
- -T4 (prohibits the dynamic scan delay from exceeding 10 ms for TCP ports. See man nmap).
- --packet-trace (Trace sent and received packets)

To scan all hostname in local network use `avahi`

- Install

      apt install avahi-daemon avahi-utils

- Run

      avahi-browse -art