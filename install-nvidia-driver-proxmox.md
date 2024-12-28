# Debian SecureBoot
Has the system booted via Secure Boot?
```
mokutil --sb-state
```
Debian uses the Dynamic Kernel Module System (DKMS) to allow individual kernel modules to be upgraded without changing the whole kernel.

Since DKMS modules are compiled individually on users own machines, it is not possible to sign DKMS modules using the Debian project's signing keys.

Instead, modules built using DKMS will be signed using a Machine Owner Key (MOK), which by default is located at /var/lib/dkms/mok.key with the corresponding public key at /var/lib/dkms/mok.pub

# Install dkms.
The NVIDIA driver installer will check for the presence of DKMS on your system. If DKMS is found, you will be given the option of registering the kernel module with DKMS. On most systems with DKMS, DKMS will take care of automatically rebuilding registered kernel modules when installing a different Linux kernel. This is typically done by hooks that Linux distributions set up to be triggered as part of the kernel installation process. If your system is not configured to automatically run DKMS to rebuild kernel modules after installing a different kernel, you may run dkms autoinstall to trigger the process manually.
```
apt install dkms

```
# Automatic Signing of DKMS-Generated Kernel Modules for Secure Boot
https://gist.github.com/lijikun/22be09ec9b178e745758a29c7a147cc9

If secure boot is enabled, kernels may require that kernel modules be cryptographically signed by a key trusted by the kernel in order to be loaded.
In order to sign the kernel module, you will need a private signing key, and an X.509 certificate for the corresponding public key. The X.509 certificate must be trusted by the kernel before the module can be loaded: we recommend ensuring that the signing key be trusted before beginning the driver installation, so that the newly signed module can be used immediately
## Step 1. Generating a MOK and Enrolling It in Secure Boot
- Start by becoming root with `sudo -i`.

- Generate the key and certificate.

      openssl req -new -x509 \
          -newkey rsa:2048 -keyout /root/nvidia-driver.key \
          -outform DER -out /root/nvidia-driver.der \
          -nodes -days 36500 -subj "/CN=Nvidia Driver Kmod Signing MOK"
          
  (The key and the certificate filenames, paths, expiration date and subject can be modified to your liking.)

- Enroll the public key.

      mokutil --import /root/nvidia-driver.der

    You'll be prompted to create a password. Enter it twice.

- Reboot the computer. At boot you'll see the MOK Manager EFI interface. Press any key to enter it.
  - "Enroll MOK"
  - "Continue".
  - "Yes". 
  - Enter the password you set up just now. 
  - Select "OK" and the computer will reboot again.
https://github.com/dell/dkms#secure-boot

- After reboot, you should be able to see the new key with `cat /proc/keys | grep asymmetri` as root.

## Step 2. Configuring DKMS to Sign Newly-Built Modules Automatically with the MOK.
- To minimize human effort and troubleshooting, it's best to get the keys, config files and scripts in place before installing any actual drivers.

- Create a text file `/etc/dkms/nvidia.conf`, or `/etc/dkms/<module-name>.conf` for other modules (with `<module-name>` part exactly matching the name of the module), which is a one-liner pointing to the signing script.

      echo "SIGN_TOOL=/root/sign-nvidia-driver.sh" > /etc/dkms/nvidia.conf
      
  (I put the script under `/root` but obviously you can adjust its path.)

- DKMS will pass to our script the kernel version number as `$1` and the full path to module file as `$2`. We'll use the `sign-file` tool from the `kernel-devel` package, which needs to be supplied with more info. 

    Create the script `/root/sign-nvidia-driver.sh` which simply provides the correct argument for `sign-file` as follows:

      #!/bin/bash
      # sign-nvidia-driver.sh
      
      hash_algo=sha256
      private_key=/root/nvidia-driver.key
      x509_cert=/root/nvidia-driver.der
      
      prefix=/usr/src/kernels/
      # For Debian/Ubuntu, use
      #prefix=/usr/src/linux-headers-
      
      "${prefix}${1}/scripts/sign-file" \
          "${hash_algo}" "${private_key}" "${x509_cert}" "${2}" \
          && echo "Signed newly-built module ${2} with MOK successfully." >&2 \
          && exit 0
      echo "Error signing file ${2}." >&2
      exit 1

    Remember to `chmod +x /root/sign-nvidia-driver.sh`.
    
    The script returns 0 when the signing succeeds and 1 when it fails. A non-zero return value will cause the DKMS build operation to fail. Corresponding message will be printed to `stderr`

# Install Nvidia driver on Proxmox Host
Download driver
```
curl -O https://us.download.nvidia.com/XFree86/Linux-x86_64/550.142/NVIDIA-Linux-x86_64-550.142.run
```
Add execution permissions
```
chmod +x NVIDIA-Linux-x86_64-550.142.run
```
Run
```
./NVIDIA-Linux-x86_64-550.142.run --dkms
```
**NOTE 1**: If error `Unable to find the development tool `cc` in your path; please make sure that you have the package 'gcc' installed` shown, install bellow package
```
apt install build-essential 
```
**NOTE 2**: If error `The nouveau kernel driver is currently in use by your system. This driver is incompatible with NVIDIA driver, and must be disabled before proceeding` shown, you want to blacklist the open source nouveau kernel module to avoid it from interfering with the one from NVIDIA.
```
echo "blacklist nouveau" >> /etc/modprobe.d/blacklist.conf
```
After changing anything modules related, you need to refresh your initramfs. On Proxmox VE this can be done by executing:
```
update-initramfs -u -k all
```
After updating initramfs, ensure that the changes take effect by rebooting your system.
To check if the modules are being loaded
```
lsmod | grep nouveau
```
**NOTE 3**: If error `unable to find the kernel source tree for the currently running kernel` shown, then install bellow package
```
apt install proxmox-headers-$(uname -r)
```

## On GUI
- Choose `Sign the kernel module`
- Choose `Use an existing key pair`
- Enter private key path
- Enter public key path
- When `Can't find X library path`, ignore and select OK
- When asked for register DKMS, select `YES`. DKMS will automatically build a new module if kernel changes later
- When asked for rn nvidia-xconfig utility and backup pre-existing X configuration, select `YES`

A reboot might be necessary at this point, after which the Nvidia drivers on the Proxmox host should now be installed. This can be confirmed by running:

    sudo nvidia-smi

Check nvidia module in "installed" state with DKMS. 
    
    dkms status

Verify if module if signed

    modinfo nvidia

To Ensure that Secure Boot enabled

    mokutil --sb-state

To view loaded NVIDIA Modules

    kmod list | grep nvidia
    lsmod | grep nvidia