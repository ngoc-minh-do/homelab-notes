# Proxy

A simplified way to sum it up would be to say that a forward proxy sits in front of a client and ensures that no origin server ever communicates directly with that specific client. On the other hand, a reverse proxy sits in front of an origin server and ensures that no client ever communicates directly with that origin server.

## Forward proxy
A forward proxy, also known as an outbound proxy, acts as an intermediary between clients and external servers, intercepting outbound requests from clients and forwarding them to their intended destinations.

Here is what forward proxies do for you:
1. Client-Side Proxying

    Forward proxies are typically deployed on the client side of a network, serving as a gateway for outbound traffic. Clients configure their network settings to route traffic through the forward proxy, which then forwards requests to external servers on behalf of the clients.

2. Anonymity and Privacy

    Forward proxies can enhance user privacy and anonymity by masking the IP addresses of clients. External servers only see the IP address of the forward proxy, making it difficult to trace the origin of requests back to individual clients.

3. Content Filtering and Caching

    Forward proxies can implement content filtering policies to restrict access to certain websites or content categories based on predefined rules. Additionally, they can cache frequently accessed content, reducing bandwidth usage and improving performance for subsequent requests.

4. Security and Access Control

    Forward proxies can also enforce security policies and access controls, allowing organizations to regulate access to external resources, block malicious websites, and inspect outbound traffic for threats or policy violations.

### Software candidates
- tinyproxy
- squid

## Reverse proxy
A reverse proxy, also known as an inbound proxy, operates on the server side of a network, serving as a front-end facade for backend servers.

It intercepts incoming requests from clients and forwards them to the appropriate back-end servers based on predefined rules.

Key aspects of reverse proxies include:

1. Server-Side Proxying

    Reverse proxies are deployed on the server side of a network, typically in front of backend web servers or application servers. They accept incoming requests from clients on behalf of backend servers and forward them internally.

2. Load Balancing and Traffic Distribution

    Reverse proxies can distribute incoming traffic across multiple backend servers to improve scalability, reliability, and performance. They use algorithms such as round-robin, least connections, or weighted distribution to evenly distribute requests.

3. SSL Termination and Encryption

    Reverse proxies can handle SSL/TLS termination, offloading the encryption and decryption process from backend servers. This simplifies management of SSL certificates and improves performance by reducing the computational overhead on backend servers.

4. Content Delivery and Optimization

    Reverse proxies can cache static content, compress data, and optimize delivery to clients, reducing latency and bandwidth usage. They can also perform content rewriting or transformation to adapt content for different client devices or browsers.

### Software candidates
- nginx
- HAProxy
- Traefik
- Caddy

### Reverse proxy with SSL certificate

## Ref
- https://www.cloudflare.com/learning/cdn/glossary/reverse-proxy/
- https://dev.to/somadevtoo/difference-between-forward-proxy-and-reverse-proxy-in-system-design-54g5