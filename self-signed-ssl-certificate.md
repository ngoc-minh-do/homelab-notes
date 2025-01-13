# Creating a Self-Signed SSL Certificate With OpenSSL

TLS/SSL functions by a combination of a public certificate and a private key. The SSL key is kept secret on the server and encrypts content sent to clients. The SSL certificate is publicly shared with anyone requesting the content. It can be used to decrypt the content signed by the associated SSL key.

You can create a self-signed key and certificate pair with OpenSSL in a single command:

    openssl req -x509 -newkey rsa:4096 -sha256 -days 3650 \
    -nodes -keyout example.com.key -out example.com.crt -subj "/CN=example.com" \
    -addext "subjectAltName=DNS:example.com,DNS:*.example.com,IP:10.0.0.1"

Here’s a breakdown of what each part of this command does:
- `req`: PKCS#10 certificate request and certificate generating command.
- `-x509`: This option outputs a certificate instead of a certificate request.
- `-nodes`: This tells OpenSSL to skip the option to secure our certificate with a passphrase. We need Nginx to be able to read the file, without user intervention, when the server starts up. A passphrase would prevent this from happening because we would have to enter it after every restart.
- `-days 3650`: This option sets the length of time that the certificate will be considered valid. We set it for 10 year here.
- `-newkey rsa:4096`: This specifies that we want to generate a new certificate and a new key at the same time. We did not create the key that is required to sign the certificate in a previous step, so we need to create it along with the certificate. The `rsa:4096` portion tells it to make an RSA key that is 4096 bits long.
- `-keyout`: Private key file output location.
- `-out`: Certificate file output location.
- `-sha256`: to generate SHA-256-based certificate
- `-subj`: Set subject name by args without interactive input. Here we provide CN (Common Name)
- `-addext`: Add a specific extension to the certificate. Here we added Subject Alternate Name (SAN)

Checking the contents of the private key

    openssl rsa -in example.com.key -noout -text
    openssl pkey -in example.com.key -check -noout

Checking the contents of the certificate

    openssl x509 -in example.com.crt -noout -text
    openssl x509 -in example.com.crt -subject -noout

If `You cannot visit right now because the website uses HSTS` error shown, consider to change public TLD (Top-Level Domain)

## Ref:
- https://www.digitalocean.com/community/tutorials/how-to-create-a-self-signed-ssl-certificate-for-nginx-in-ubuntu
- https://stackoverflow.com/questions/10175812/how-to-generate-a-self-signed-ssl-certificate-using-openssl
- https://youtu.be/VH4gXcvkmOY?si=st5uPlRC7QnF1L1N
- https://www.youtube.com/watch?v=EnY6fSng3Ew