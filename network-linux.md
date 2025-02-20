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
```
ifdown enp7s0
ifup enp7s0
```
Force an Interface release & request new ip from DHCP server for specific interface
```
sudo dhclient -r <interface>
sudo dhclient <interface>
```
Modify `/etc/network/interfaces`
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
**NOTE** 
- If setting multiple interfaces with static ip, `gateway` properties should be defined for 1 interface only 
- If `RTNETLINK answers: file exists` error shown, try bellow command to clear assigned ip address
```
sudo ip addr flush <interface>
```
Restart network service
```
sudo systemctl restart networking.service
```
## Setting DNS
To make it use the DHCPv4 protocol to obtain dns servers address
```
sudo dhclient -4
```
To manual config DNS, modify `/etc/resolv.conf`
```
nameserver 192.168.0.1
nameserver 8.8.8.8
```
**NOTE**: Make sure there is no interface with dhcp setting in `/etc/network/interfaces`, otherwise this file will be overwritten 

Confirm DNS
```
ip route
nslookup google.com
traceroute google.com
dig google.com
```
Ref:
- https://wiki.debian.org/resolv.conf
- https://manpages.debian.org/bookworm/isc-dhcp-client/dhclient.8.en.html

## Disable ipv6
 
Add the following at the bottom of the file `/etc/sysctl.conf`
```
net.ipv6.conf.all.disable_ipv6 = 1
net.ipv6.conf.default.disable_ipv6 = 1
net.ipv6.conf.lo.disable_ipv6 = 1
```
Then run
```
sysctl -p
```
Ref:
- https://support.nordvpn.com/hc/en-us/articles/20164669224337-How-to-disable-IPv6-on-Linux

## Manage route

Find current default gateway
```
ip route show 0.0.0.0/0
```
Manage route
```
ip route add {NETWORK} via {IP} dev {DEVICE}
sudo ip route add 89.187.160.1/32 via 192.168.1.1 dev enp6s16
```
Ref: https://www.cyberciti.biz/tips/configuring-static-routes-in-debian-or-red-hat-linux-systems.html/

## Ping using specific NIC
```
ping google.com -I enp6s16
```
## Test real network speed

Install `iperf3`
```
apt install iperf3
```
Find a `iperf3 server` address on google, then test speed by
```
iperf3 -c <iperf3 server>
iperf3 -c <iperf3 server><device>
iperf3 -c 89.187.160.1%enp6s16
```
Ref: https://iperf2.sourceforge.io/iperf-manpage.html

## Trace route
  
Perform traceroute using specific internet interface
```
traceroute -i eth0 google.com
```
Trace route to a service (Windows)
```
tracert 8.8.8.8
```
## Scan Local network

Scan all ip in local network
```
nmap -sn 192.168.0.*
```
Scan all ip and port
```
nmap 192.168.0.*
```
Flags have the following meanings:
- -vv (Increase verbosity)
- -n (No DNS resolution. This speeds up our scan!)
- -sn (No port scan)
- -PE (Use ICMP echo request queries. This is what is displayed in the output above)
- -T4 (prohibits the dynamic scan delay from exceeding 10 ms for TCP ports. See man nmap).
- --packet-trace (Trace sent and received packets)

To scan all hostname in local network use `avahi`

- Install
```
apt install avahi-daemon avahi-utils
```
- Run
```
avahi-browse -art
```
## Check listing port
```
sudo lsof -i -P -n
less /etc/services
```
## Test connection to a website by fetching web content from CLI
```
curl -L $url
wget -O - $url
```
## Multicast DNS (mDNS)
To setup mDNS
```
sudo apt install avahi-daemon
sudo systemctl start avahi-daemon
sudo systemctl enable avahi-daemon
```
Then we can use `<hostname>.local` to access