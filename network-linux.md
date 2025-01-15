# Network on Linux

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
Starting and Stopping Interfaces

    # ifdown enp7s0
    # ifup enp7s0

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
iface enp0s5 inet static
    address 192.168.0.20/24
    gateway 192.168.0.1
```
**Note**: Comment out ipv6 setting if you don't want `dhclient` fetching DNS server ipv6
```
sudo systemctl restart networking.service
```

## Disable ipv6
 
Add the following at the bottom of the file `/etc/sysctl.conf`

    net.ipv6.conf.all.disable_ipv6 = 1
    net.ipv6.conf.default.disable_ipv6 = 1
    net.ipv6.conf.lo.disable_ipv6 = 1

Then run

    sysctl -p

Ref:
- https://support.nordvpn.com/hc/en-us/articles/20164669224337-How-to-disable-IPv6-on-Linux

## Configure DNS Server - resolv.conf
To make it use the DHCPv4 protocol to obtain an IPv4 address, dns server...

    dhclient -4

Ref:
- https://wiki.debian.org/resolv.conf
- https://manpages.debian.org/bookworm/isc-dhcp-client/dhclient.8.en.html
## Trace route
  
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

## Multicast DNS (mDNS)
To setup mDNS

    sudo apt install avahi-daemon
    sudo systemctl start avahi-daemon
    sudo systemctl enable avahi-daemon

Then we can use `<hostname>.local` to access

## Test connection to a website by fetching web content from CLI

    curl -L $url
    wget -O - $url