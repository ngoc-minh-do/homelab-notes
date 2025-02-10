# Send log to remote server

## Using Syslog
Install `rsyslog`

    apt update && apt install rsyslog

Setting `rfc5424` log format for forwarding. Modify `/etc/rsyslog.conf`

    $ActionForwardDefaultTemplate RSYSLOG_SyslogProtocol23Format

Add forwarding config

     echo '*.* @@remote-host:port' > /etc/rsyslog.d/promtail.conf

Note: `@` for UDP, `@@` for TCP protocol

Restart `rsyslog`

    sudo systemctl restart syslog

## Using Journal

### On Server side
Install

    sudo apt install systemd-journal-remote

Modify `/lib/systemd/system/systemd-journal-remote.service`
- to use `http`, change `--listen-https=-3` to `--listen-http=-3`
- Change `LogsDirectory` if needed

Modify `/lib/systemd/system/systemd-journal-remote.socket`
- Change `ListenStream` (port number) if needed

Enable & start service

    sudo systemctl enable --now systemd-journal-remote.service

### On client side
Install

    sudo apt install systemd-journal-remote

Modify `/etc/systemd/journal-upload.conf`

    URL=http://<host>:19532

Enable & start service

    sudo systemctl enable --now systemd-journal-upload.service 