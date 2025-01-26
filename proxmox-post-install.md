# Proxmox post install

## Correct sources to update and install packages

    cat <<EOF >/etc/apt/sources.list
    deb http://deb.debian.org/debian bookworm main contrib
    deb http://deb.debian.org/debian bookworm-updates main contrib
    deb http://security.debian.org/debian-security bookworm-security main contrib
    EOF
    # Optional ?!
    # echo 'APT::Get::Update::SourceListWarnings::NonFreeFirmware "false";' >/etc/apt/apt.conf.d/no-bookworm-firmware.conf

## Disabling 'pve-enterprise' repository

    cat <<EOF >/etc/apt/sources.list.d/pve-enterprise.list
    # deb https://enterprise.proxmox.com/debian/pve bookworm pve-enterprise
    EOF

## Enabling 'pve-no-subscription' repository

    cat <<EOF >/etc/apt/sources.list.d/pve-install-repo.list
    deb http://download.proxmox.com/debian/pve bookworm pve-no-subscription
    EOF

## Disable "No Valid Subscription" dialog

    sudo sed -i '/.*data\.status.*{/{s/\!//;s/active/NoMoreNagging/}' /usr/share/javascript/proxmox-widget-toolkit/proxmoxlib.js
    sudo sed -i '/.*data\.status.*{/{s/\!//;s/active/NoMoreNagging/}' /usr/share/pve-manager/touch/pvemanager-mobile.js

## Ref
- https://community-scripts.github.io/ProxmoxVE/scripts?id=post-pve-install