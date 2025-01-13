# ACME

## ACME protocol
The `Automated Certificate Management Environment` protocol (ACME) is a protocol for automating certificate lifecycle management communications between Certificate Authorities (CAs) and a company’s web servers, email systems, user devices, and any other place Public Key Infrastructure certificates (PKI) are used. The ACME protocol has no licensing fees, and it requires very little time for IT teams to configure and execute their certificate management automation, making it an increasingly adopted component of enterprise security.


## A Typical ACME Flow
Here's how an ACME client might request an X.509 certificate from a CA.

1. The ACME client creates an account with an ACME CA server and submits a certificate order. You can think of an ACME account as a place to store open certificate requests for that particular client.
2. The CA responds with a set of challenges. To complete the challenges, the client must prove it controls each subject name (domain name, IP address, or hardware device ID) that it is requesting in the certificate.
3. The CA verifies the client's challenge responses.
4. Once the client successfully completes the ACME challenges, it submits a certificate signing request (CSR) to the CA.
5. The CA verifies that the client has control of the private key associated with the certificate request.
6. The CA issues a certificate to the client.

The ACME API for certificate requests requires an HTTPS connection between the client and CA.

## ACME Challenge

### 1. The HTTP Challenge (http-01)

The ACME CA challenges the client to host a random number at a random URL under /.well-known/acme-challenge on port 80. The CA verifies client control by issuing an HTTP GET request to that URL.

When To Use It

This is a good general-purpose challenge type. By hosting the challenge response via HTTP on port 80, the client proves its control over a protected port on the domain being requested. The http-01 challenge type is the easiest to set up, because any web server will let you host the challenge response as a static file.

### 2. The DNS Challenge (dns-01)
The ACME CA challenges the client to provision a random DNS TXT record for the domain in question. It verifies the challenge by querying DNS for that TXT record.

After the verification process completed the DNS TXT record will be removed

When To Use It

The dns-01 challenge type is good if your ACME server cannot reach the requested domain directly. The server only needs to be able to perform a DNS lookup to confirm the challenge. However, because the ACME client needs to modify DNS records, configuring a dns-01 client is usually more involved.

### 3. The TLS ALPN challenge (tls-alpn-01)
The ACME CA uses TLS to validate a challenge, leveraging application layer protocol negotiation (ALPN) in the TLS handshake. The client presents a self-signed TLS certificate containing the challenge response as a special X.509 certificate extension.

When To Use It

This challenge type is useful when a security policy requires the CA to reach the client via a TLS connection. This is a popular challenge type in cases where an ingress controller fronts clients attempting to receive a certificate.

### 4. The Device Attestation Challenge (device-attest-01)
The device attestation challenge (device-attest-01) is designed to issue client certificates bound to a device identifier.

It allows clients with an attached security module (TPM, Secure Enclave, Yubikey, etc) to request a certificate bound to the security module's permanent hardware identifier. It can also be used to attest the hardware protection of a private key in the security module.

## Let’s Encrypt

To enable HTTPS on your website, you need to get a certificate (a type of file) from a Certificate Authority (CA). Let’s Encrypt is a CA. In order to get a certificate for your website’s domain from Let’s Encrypt, you have to demonstrate control over the domain. With Let’s Encrypt, you do this using software that uses the ACME protocol which typically runs on your web host.

Certificates are valid for only 90 days

## Ref
- https://smallstep.com/docs/step-ca/acme-basics/#overview
- https://letsencrypt.org/getting-started/