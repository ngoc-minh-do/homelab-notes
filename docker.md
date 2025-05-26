# Docker

Create volume
```
docker volume create hello
docker volume create --name hello \
    --driver local \
    --opt type=none \
    --opt device=/hello \
    --opt o=bind
```
Execute a command in container
```
sudo docker exec <container-name> <program-name> <argument>
```

Show docker disk usage
```sh
docker system df
```
## Docker Swarm
On Manager node
```
docker swarm init --advertise-addr <MANAGER-IP>
```
On Worker node
```
docker swarm join \
  --token <token> \
  <MANAGER-IP>:2377
```
Verify
```
docker info
docker service ls
docker stack ls
docker node ls
```
Change node availability to `drain`
```
docker node update --availability drain node-1
```
## Portainer in Swarm mode
```
docker stack deploy -c portainer-agent-stack.yml portainer-agent
```
## Networks
Create overlay network
```
docker network create \
  --driver overlay \
  --subnet 10.0.10.0/24 \
  --attachable \
  reverse-proxy
```
## Compose
```
docker compose up -d
docker compose up -d --force-recreate
docker compose up -d --force-recreate --build
```
Options:
- `-d`: detach mode
- `--force-recreate`: Force recreate container
- `--build`: force the container to be rebuilt, use full when container is build from `dockerfile`

Destroy
```
docker compose down
docker compose -p <compose-name> down
```