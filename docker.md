# Docker

Create volume

    docker volume create hello
    docker volume create --name hello \
        --driver local \
        --opt type=none \
        --opt device=/hello \
        --opt o=bind

## Docker Swarm
On Manager node

    docker swarm init --advertise-addr <MANAGER-IP>

On Worker node
    docker swarm join \
      --token <token> \
      <MANAGER-IP>:2377

Verify

    docker info
    docker service ls
    docker stack ls
    docker node ls

Change node availability to `drain`

    docker node update --availability drain node-1

## Portainer in Swarm mode

    docker stack deploy -c portainer-agent-stack.yml portainer-agent

## Networks
Create overlay network

    docker network create \
      --driver overlay \
      --subnet 10.0.10.0/24 \
      --attachable \
      reverse-proxy