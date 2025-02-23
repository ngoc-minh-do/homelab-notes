# Setup Reverse Proxy

## Map hostnames to IP addresses

### Option 1: Modify host file
```
192.168.x.x       domain.local
```
### Option 2: Modify internal DNS server setting

## Reverse Proxy with Self signed SSL certificate

### Create Self signed SSL certificate
Refer to [self-signed-ssl-certificate](self-signed-ssl-certificate.md)

### Using nginx

Create `/etc/nginx/conf.d/domain.local.conf`
```
server {
	listen 443 ssl;
	listen [::]:443 ssl;
	ssl_certificate /etc/nginx/conf.d/domain.local.crt;
	ssl_certificate_key /etc/nginx/conf.d/domain.local.key;

	server_name domain.local www.domain.local;
		
	location / {
		proxy_pass http://192.168.x.x:xxxx;
		proxy_set_header Host $http_host;
		proxy_set_header X-Real-IP $remote_addr;
		proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
		proxy_set_header X-Forwarded-Proto $scheme;
	}
}
```
Confirm nginx config
```
nginx -t
```
Restart nginx
```
nginx -s reload
```
### Using traefik
Modify `/etc/traefik/traefik.yaml`, add
```
providers:
  file:
	directory: "/etc/traefik/dynamic"
	watch: true
```
Add `/etc/traefik/dynamic/something.yaml`
```
http:
  routers:
	router0:
	  rule: Host(`domain.local`)
	  service: service-foo
	  tls: {}

  services:
	service-foo:
	  loadBalancer:
		servers:
		- url: http://192.168.x.x:xxxx

tls:
  stores:
	default:
	  defaultCertificate:
		certFile: /etc/traefik/domain.local.crt
		keyFile: /etc/traefik/domain.local.key
  certificates:
	- certFile: /etc/traefik/domain.local.crt
	  keyFile: /etc/traefik/domain.local.key
	  stores:
		- default
```
### Ref
- https://akashrajpurohit.com/blog/nginx-the-reverse-proxy-in-my-homelab/
- https://www.digitalocean.com/community/tutorials/how-to-create-a-self-signed-ssl-certificate-for-nginx-in-ubuntu-20-04-1
- https://phoenixnap.com/kb/nginx-reverse-proxy
- https://docs.nginx.com/nginx/admin-guide/web-server/reverse-proxy/


## Reverse Proxy with Let's Encrypt SSL certificate 

### Using traefik

Modify `/etc/traefik/traefik.yaml`, add

```
providers:
  file:
	directory: "/etc/traefik/dynamic"
	watch: true

certificatesResolvers:
  letsencrypt:
	acme:
	  storage: /letsencrypt/acme.json
	  email: name@mail.com
	  # caServer: "https://acme-staging-v02.api.letsencrypt.org/directory" # Staging
	  caServer: "https://acme-v02.api.letsencrypt.org/directory"
	  dnsChallenge:
		provider: cloudflare
		resolvers:
		  - "1.1.1.1:53"
		  - "1.0.0.1:53"
```
Add `/etc/traefik/dynamic/something.yaml`
```
http:
  routers:
	traefik:
	  rule: Host(`traefik.subdomain.domain.com`)
	  middlewares:
		- traefik-auth
		- secured
	  service: api@internal
	  tls:
		certResolver: letsencrypt
		domains:
		  - main: subdomain.domain.com
			sans:
			  - "*.subdomain.domain.com"

	middlewares:
	  traefik-auth:
		basicAuth:
		  usersFile: /etc/traefik/.htpasswd

	  secured:
		chain:
		  middlewares:
			- default-ipAllowList

	  default-ipAllowList:
		ipAllowList:
		  sourceRange:
			- 127.0.0.1/24
			- 192.168.0.0/24
			- 172.22.0.0/24
```

## Verify proxy without modify host file
```
curl -H Host:domain.local -Lk http://192.168.x.x:xxxx
```
- `-H` Add header
- `-k` insecure
- `-L` Follow redirection