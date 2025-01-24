# Crowdsec

## Basic command
Show overview of CrowdSec statistics

    cscli metrics
    cscli metrics show decisions

Manage ban list

    cscli decisions list
    cscli decisions add --ip 192.168.x.x
    cscli decisions delete --ip 192.168.x.x

Manage alert list

    cscli alert list
    cscli alert inspect 123
    cscli alert delete 123

Install Hub collection (parser, etc...)

    cscli collections install crowdsecurity/linux
    cscli collections list

Update Hub collection, parser, etc...

    cscli hub update
    cscli hub upgrade

Add bouncer

    sudo docker exec crowdsec cscli bouncers add traefik-bouncer

Manage notification

    sudo docker exec crowdsec cscli notifications list
     sudo docker exec crowdsec cscli notifications test email_default

## Refer
- https://www.crowdsec.net/blog/enhance-docker-compose-security
- https://docs.crowdsec.net/docs/appsec/quickstart