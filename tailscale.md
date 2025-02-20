# Tailscale

## Connect to Tailscale as a subnet router

Enable IP forwarding
```
echo 'net.ipv4.ip_forward = 1' | sudo tee -a /etc/sysctl.d/99-tailscale.conf
echo 'net.ipv6.conf.all.forwarding = 1' | sudo tee -a /etc/sysctl.d/99-tailscale.conf
sudo sysctl -p /etc/sysctl.d/99-tailscale.conf
```
Ref: https://tailscale.com/kb/1019/subnets?tab=linux#enable-ip-forwarding