# VPN（Virtual Private Network）

TODO

### Software candidates
- wireguard
- OpenVPN
- Gluetun (support multiple commercial integrations)

## VPS (Virtual Private Server)

TODO

## Jump server vs Bastion server

- A `Bastion host` is a machine that is outside of your security zone.

      And is expected to be a weak point, and in need of additional security considerations.
      Because your security devices are technically outside of your security zone, firewalls and security appliances are also considered in most cases Bastion hosts.
      Usually we're talking about:
      - DNS Servers
      - FTP Servers
      - VPN Servers

- A `Jump Server` is intended to breach the gap between two security zones.

      The intended purpose here is to have a gateway to access something inside of the security zone, from the DMZ.