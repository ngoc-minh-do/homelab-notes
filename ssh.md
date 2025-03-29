# ssh

## ssh-keygen
```
ssh-keygen -t ed25519 -C "your_email@example.com"
```

Options:

    -b bits
            Specifies the number of bits in the key to create.  For
            RSA keys, the minimum size is 1024 bits and the default
            is 3072 bits. Generally, 3072 bits is considered
            sufficient. DSA keys must be exactly 1024 bits as
            specified by FIPS 186-2. For ECDSA keys, the -b flag
            determines the key length by selecting from one of three
            elliptic curve sizes: 256, 384 or 521 bits. Attempting
            to use bit lengths other than these three values for
            ECDSA keys will fail. ~~ECDSA~~-SK, Ed25519 and Ed25519-SK
            keys have a fixed length and the -b flag will be ignored.

    -C comment
            Provides a new comment.

    -t dsa | ecdsa | ecdsa-sk | ed25519 | ed25519-sk | rsa
            Specifies the type of key to create.  The possible values
            are “dsa”, “ecdsa”, “ecdsa-sk”, “ed25519”, “ed25519-sk”,
            or “rsa”.

            This flag may also be used to specify the desired
            signature type when signing certificates using an RSA CA
            key. The available RSA signature variants are “ssh-rsa”
            (SHA1 signatures, not recommended), “rsa-sha2-256”, and
            “rsa-sha2-512” (the default).

|Algorithm|Key Size (bits)|Security Level|Speed|Use Case|Strengths|Weaknesses|
|---|---|---|---|---|---|---|
|RSA|1024 - 4096|High|Slow|Digital Signatures, TLS|Well-studied, widely used.|Potentially vulnerable to quantum computing attacks.|
|DSA|1024 - 3072|Moderate to High|Fast|Digital Signatures|Faster than RSA.|Fixed key size.|
|ECDSA|256 - 521|High|Very Fast|Digital Signatures|Smaller key size, high security.|Complex implementation.|
|Ed25519|256|Very High|Very Fast|Digital Signatures|High security, fast, small keys.|Newer, not widely supported.|
|SSH-1 (RSA)|768 - 2048|Low to Moderate|Slow|Secure Shell (SSH)|Initial SSH protocol.|Deprecated, vulnerable.|

## ssh client
```
apt install openssh-client
```
Client configuration file

	/etc/ssh/ssh_config.d/*.conf

Connect with password
```
ssh $remote_user@$remote_host
```

Connect with private key
```
ssh username@server -i '/path/to/keyfile'
```

Start SSH agent
1. On Linux
```
eval "$(ssh-agent)"
```

1. On Windows
```
Get-Service -Name ssh-agent | Set-Service -StartupType Automatic
Start-Service ssh-agent
```

Connect with private key and save authentication information to `ssh-agent`
```
ssh username@server -i '/path/to/keyfile' -o AddKeysToAgent=yes
```

Add your private key to SSH agent
```
ssh-add
ssh-add ~/.ssh/id_ed25519
```

To check saved key
```
ssh-add -l
```

Otherway is set it in `~/.ssh/config`.
Other useful option is:
```
AddKeysToAgent yes              # as mention before
IdentityFile ~/.ssh/xxx         # to specific private key if needed
LogLevel DEBUG                  # to check log
UseKeychain yes                 # for mac
```

We can also set friendly name for each host in `~/.ssh/config`

For Linux, to keep `ssh-agent` running, add bellow line to `~/.bashrc` or `~/.zshrc`
```sh
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
```

**Ref**
- https://man7.org/linux/man-pages/man1/ssh.1.html
- https://man7.org/linux/man-pages/man5/ssh_config.5.html

## ssh server
```
apt install openssh-server
```
Server configuration file:  `/etc/ssh/sshd_config.d/*.conf`

**NOTE**: Make sure bellow line exist in `/etc/ssh/sshd_config`
```
Include /etc/ssh/sshd_config.d/*.conf
```

Save client's public key to below file
```
vi /home/user_name/.ssh/authorized_keys
```

Set
```
chmod 700 /home/user_name/.ssh
chmod 600 /home/user_name/.ssh/authorized_keys
chown -R username:username /home/username/.ssh
```
`-R` is recursive

Check log
```
journalctl -u ssh -n 50
```

### Disable password login
Signing in as root is typically achieved by signing in as your normal user id then using `sudo`

Create new config file, for example `/etc/ssh/sshd_config.d/disable_password_login.conf`
```
PasswordAuthentication no
ChallengeResponseAuthentication no
UsePAM no
PermitRootLogin no
```

Where,
- `ChallengeResponseAuthentication` – State whether challenge-response authentication is allowed or not via PAM.
- `PasswordAuthentication` – Configure whether password authentication is allowed or not.
- `UsePAM` – Enables the Pluggable Authentication Module interface. If set to yes this will enable PAM authentication using ChallengeResponseAuthentication and PasswordAuthentication in addition to PAM account and session module processing for all authentication types.
- `PermitRootLogin` – Specifies whether root can log in using ssh or not.

Reload
```
systemctl reload sshd
# CentOS
systemctl reload ssh #
```
## sudo

- `sudo`: Super User DO
- `su`: Substitute User

Switch to user. 
```
su - <user>
sudo -iu <user>
```

Switch to root
```
su -
sudo -i
```

**NOTE**: 
- `sudo` uses the current users' password default config. `su` uses the password of the user you're trying to run as.
- `sudo -i` keep inherit `env`

Check current user
```
whoami
```