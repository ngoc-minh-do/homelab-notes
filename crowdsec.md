# Crowdsec

## Basic command
Show overview of CrowdSec statistics

    cscli metrics
    cscli metrics show decisions

Manage ban list

    cscli decisions list
    cscli decisions add --ip 192.168.x.x
    cscli decisions delete --ip 192.168.x.x

Install Hub collection (parser, etc...)

    cscli collections install crowdsecurity/linux

Update Hub collection, parser, etc...

    cscli hub update
    cscli hub upgrade