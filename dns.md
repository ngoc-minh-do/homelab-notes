# DNS

## DNS record
The most common types of DNS records are:
1. A records

    Address records, or A records, are the most common DNS records used. They create a direct connection between an IPv4 address and a domain name. IPv4 addresses have the following format: 93.184.216.34.

2. AAAA records

    Like A records, this type of record connects domain names to IPv6 addresses. IPv6 addresses have more numerals than IPv4 address and are becoming more common as options for IPv4 addresses are running out.

3. CNAME records

    Canonical name records, or CNAME records, direct an alias domain to a canonical domain. This means that this type of record is used to link subdomains to domain A or AAAA records.

    For example, instead of creating two A records for www.example.com and product.example.com, you could link product.example.com to a CNAME record that is then linked to an A record for example.com. The value is that if the IP address changes for the root domain, only the A record will have to be updated and the CNAME will update accordingly.

4. DNAME records

    Delegation name records, or DNAME records, are used to redirect multiple subdomains with one record and point them to another domain.

    For example, a DNAME record linking domain.com to example.com will link product.domain.com, trial.domain.com, and blog.domain.com to example.com. These records are helpful in managing largescale domains and in managing domain name changes by ensuring subdomains are properly linked.

5. CAA records

    Certification authority authorization records, or CAA records, allow domain owners to specify which certificate authorities (CAs) can issue certificates for their domain. A CA is an organization that validates the identity of websites and connects them to cryptographic keys by issuing digital certificates.

6. CERT records

    Certificate, or CERT records, store certificates that verify the authenticity of all parties involved. This type of record is particularly valuable when securing and encrypting sensitive information.

7. MX records

    Mail exchange, or MX records, direct emails to your domain mail server. These records, along with an email server, allow for the creation of individual email accounts, such as user@example.com, that are linked to the domain (example.com).

8. NS records

    Nameserver, or NS records, show which DNS server is acting as the authoritative nameserver for your domain. Authoritative nameservers contain the final information about a specific domain and its corresponding IP address. An NS record points to all of the different records your domain holds. Without NS records, users will not be able to access your website.

9. SOA records

    Start of authority, or SOA records, store important administrative information about a domain. This information can include the domain administrator’s email address, information on domain updates and when a server should refresh its information.

10. PTR records

    Pointer records, or PTR records, work in the opposite direction of A records. They are used to connect an IP address with a domain name, instead of a domain name with an IP address. When a DNS lookup begins with an IP address, it then finds the corresponding hostname. These records are used to detect spam by checking if the IP addresses and associated email addresses are used by legitimate email servers. PTR records must be set up by the server host.

11. SPF records

    Sender policy framework, or SPF records, are used to identify the mail servers that can send emails through your domain. This helps prevent your domain from being used by spammers or for malicious purposes by letting email receivers know that what they are receiving has been authorized.

12. SRV records

    Service, or SRV records, identify a host and port for specific services, such as messaging, for a domain. Ports are virtual connection points that allow digital devices to separate different types of traffic.

13. ALIAS record

    ALIAS records are used to direct your domain name to a host name and not an IP address. For instance, if your domain name is example.com, you can point it to product.differentexample.com using an ALIAS record.

14. NSEC records

    Next secure records, or NSEC records, allow for proof of non-existence. This means that these records exist to confirm that other records do not exist. Being able to confirm the non-existance of a record saves time when searching for specific records.

15. URLFWD records

    URL forwarding (or URL redirecting) is a technique used to make a single web page available via multiple URLs. NS1 Connect users can easily set up URL forwarding (HTTP redirects or masking) between zones. There are three types of URL redirects: Permanent (301), temporary (302), or masking.

16. TXT records

    Text, or TXT records, store textual information related to domains and subdomains. Text records allow for the storage of SPF records and email verification records. DKIM and DMARC records, which are stored in TXT records, help email servers confirm that a message is coming from a reliable source.

## Check DNS record

    nslookup domain.com

## Domain Registrar

- Cloudflare
- Namecheap
- Porkbun

## Internal DNS Server candidates
- Pi-hole
- Technitium DNS
- Adguard Home

## Dynamic DNS

Dynamic DNS (DDNS) is an extension of DNS that automatically updates IP addresses associated with domain names in real time.

### Provider candidate

- Cloudflare
- DuckDNS

## Ref
- https://www.ibm.com/think/topics/dns-records