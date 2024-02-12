# FreeBird
A guide for self-hosting a Nitter instance

🚧 WIP 🚧

```
docker compose run --build nitter-auth
docker compose up --scale nitter-auth=0
```

```
docker compose -f docker-compose.nitter.yml up --scale nitter-auth=0
```