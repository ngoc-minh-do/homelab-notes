# ssh

    ssh-keygen -t ed25519 -C "your_email@example.com"

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