# Home assistant

## Prepare image
Copy link of KVM file from HA website

In proxmox

    wget <ADDRESS>

Expand the compressed image

    unxz </path/to/file.qcow2.xz>

## Create VM

- OS:
  - Select 'Do not use any media'

- System:
  - Change 'machine' to 'q35'​【11 m】
  - Change BIOS to OVMF (UEFI)
  - Select the EFI storage (typically local-lvm/zfs)

- Disks:
  - Delete the SCSI drive and any other disks

Confirm and finish. Do not start the VM yet.

## Add the image to the VM

In console, use the following command to import the image from the host to the VM

    qm importdisk <VM ID> </path/to/file.qcow2> <EFI location>

For example,

    qm importdisk 205 /home/user/haos_ova-12.0.qcow2 local-lvm

In proxmox Web, select your HA VM
- Go to the 'Hardware' tab
- Select the 'Unused Disk' and click the 'Edit' button
- Check the 'Discard' box if you're using an SSD then click 'Add'
- Remove ROM/DVD device
- Select the 'Options' tab
- Select 'Boot Order' and hit 'Edit'
- Check the newly created drive (likely scsi0) and move is to the top

Finish Up
- Start the VM
- When `proxmox` logo showup, hit ESC, disable `secure boot`. Restart
- Check the shell of the VM. If it booted up correctly, you should be greeted with the link to access the Web UI.
- Navigate to <VM IP>:8123

Done. Everything should be up and running now.

## Configuration

### Sesame

/homeassistant/configuration.yaml
```yaml
sensor:
  - platform: rest
    name: Entrance Lock Sensor
    resource: https://app.candyhouse.co/api/sesame2/E0A1yyyy-yyyy-yyyy-yyyy-yyyyyyyyyyyy
    headers:
      x-api-key: 4Zb4xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
    value_template: '{{ value_json.CHSesame2Status }}'
    json_attributes:
      - batteryPercentage
      - batteryVoltage
      - position
      - CHSesame2Status
      - timestamp
    scan_interval: 3600

shell_command:
  lock_entrance_lock: ./scripts/sesame.py lock 4Zb4xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx E0A1yyyy-yyyy-yyyy-yyyy-yyyyyyyyyyyy 0000cf3cf3cf3cf3cf3cf3cf3cf3cf3c
  unlock_entrance_lock: ./scripts/sesame.py unlock 4Zb4xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx E0A1yyyy-yyyy-yyyy-yyyy-yyyyyyyyyyyy 0000cf3cf3cf3cf3cf3cf3cf3cf3cf3c

lock:
  - platform: template
    unique_id: lock.entrance_lock
    name: Entrance Lock
    value_template: "{{ is_state('sensor.entrance_lock_sensor', 'locked') }}"
    lock:
      service: shell_command.lock_entrance_lock
    unlock:
      service: shell_command.unlock_entrance_lock
```
`sesame.py` location:

    /homeassistant/scripts/sesame.py

Assign permission

    sudo chmod 755 /etc/homeassistant/bin/sesame
Try

    /etc/homeassistant/bin/sesame --help

Ref:
- https://document.candyhouse.co/demo/webapi-en
- https://www.home-assistant.io/integrations/sensor.rest/
- https://www.home-assistant.io/integrations/shell_command/
- https://www.home-assistant.io/integrations/lock.template/
- https://rewse.jp/blog/control-sesame-home-assistant/