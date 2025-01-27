# pfSense

## Installation guide for install on Proxmox

https://docs.netgate.com/pfsense/en/latest/recipes/virtualize-proxmox-ve.html

## Allow access from Wan
Option 1: Using `Shell`, from console select option 8

    pfSsh.php playback enableallowallwan


Option 2: Using `PHP Shell`, from console select option 8

    playback enableallowallwan

After done with access from Wan, remove the “allow all” rule from the WAN

Ref:
- https://docs.netgate.com/pfsense/en/latest/troubleshooting/locked-out.html#add-an-allow-all-wan-rule-from-the-shell
- https://docs.netgate.com/pfsense/en/latest/development/php-shell.html#enableallowallwan

## Add  access from Wan
Option 1: Using Web GUI

    Define additional hostnames under `System > Advanced, Admin Access` tab in the `Alternate Hostnames` field

Option 2: Modify /conf/config.xml

    <pfsense>
      <system>
        <webgui>
          <althostnames>pfsense.example.com</althostnames>
        </webgui>
      </system>
    </pfsense>

Run `rm /tmp/config.cache` to clear the configuration cache

From console select option 11 `restart webConfigurator`

Ref:
- https://docs.netgate.com/pfsense/en/latest/services/dns/rebinding.html#gui-protection
- https://docs.netgate.com/pfsense/en/latest/config/xml-configuration-file.html#edit-in-place