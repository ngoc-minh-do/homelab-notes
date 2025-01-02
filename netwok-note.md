# Network note

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

Trace route to a service (Windows)

    tracert 8.8.8.8

To scan all hostname in local network use `avahi`

- Install

      apt install avahi-daemon avahi-utils

- Run

      avahi-browse -art