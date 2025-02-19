# Debian Desktop Environment

## Install XFCE desktop environment

```
sudo apt install xfce4 xfce4-goodies -y
```

Reboot 
```
sudo reboot
```

## (Optional) Install remote desktop

### Install `Xrdp`
```
sudo apt install xrdp -y
```

Confirm `Xrdp`
```
sudo systemctl status xrdp
```

### Add user xrdp into ssl-cert group
A certificate known as a key file and located at `/etc/ssl/private/ssl-cert-snakeoil.key` is important to create a successful connection between the remote and client machine.

Otherwise, `[ERROR] Cannot read private key file /etc/xrdp/key.pem: Permission denied` error will be shown

```
sudo adduser xrdp ssl-cert
```
### Configure xrdp to use XFCE

Users need to allow **xrdp** to initiate XFCE for incoming RDP connections.

Modify `/etc/xrdp/startwm.sh` and comment out below and add `startxfce4` at the end of line
```
# test -x /etc/X11/Xsession && exec /etc/X11/Xsession
# exec /bin/sh /etc/X11/Xsession
startxfce4
```

Restart the **xrdp** service:
```
sudo systemctl restart xrdp
```

**NOTE**
- If `Failed to execute child process “dbus-launch”` error shown when trying remote desktop, install
```
apt-get install -y dbus-x11
```
### Install Chrome

```
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo apt install -y ./google-chrome-stable_current_amd64.deb
rm ./google-chrome-stable_current_amd64.deb 
```
### Enable sound when using xrdp
- pulseaudio-module-xrdp
	https://github.com/neutrinolabs/pulseaudio-module-xrdp
- xRDP installer script
	https://www.c-nergy.be/products.html
## Reference
- https://phoenixnap.com/kb/debian-remote-desktop
- https://learn.microsoft.com/en-us/azure/virtual-machines/linux/use-remote-desktop?tabs=azure-cli