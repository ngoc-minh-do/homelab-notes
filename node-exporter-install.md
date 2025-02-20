# Node Exporter install

Download
```
wget https://github.com/prometheus/node_exporter/releases/download/v1.8.2/node_exporter-1.8.2.linux-amd64.tar.gz
tar xvfz node_exporter-*.*-amd64.tar.gz
```
Copy to `/usr/bin/` and setup permission
```
sudo cp node_exporter-1.8.2.linux-amd64.tar.gz/node_exporter /usr/bin/
sudo chown <your-user>:<your-user> /usr/bin/node_exporter
```
Make Node Exporter run at boot by creating a service file
```
sudo vi /usr/lib/systemd/system/node_exporter.service
```
Add the following configuration
```
[Unit]
Description=Node Exporter
Documentation=https://prometheus.io/docs/guides/node-exporter/
Wants=network-online.target
After=network-online.target

[Service]
User=<your-user>
Group=<your-user>
Type=simple
Restart=always
ExecStart=/usr/bin/node_exporter

[Install]
WantedBy=multi-user.target
```
Install service
```
sudo systemctl daemon-reload
sudo systemctl enable node_exporter
sudo systemctl start node_exporter
```
## Ref
- https://prometheus.io/docs/guides/node-exporter
- https://developer.couchbase.com/tutorial-node-exporter-setup

