# FreeBird
A guide for self-hosting a Nitter instance

🚧 WIP 🚧

## Why

## What can you expect

## Prerequisites

## How-to

```
docker compose run --build nitter-auth
docker compose up --scale nitter-auth=0
```

```
docker compose -f docker-compose.nitter.yml up --scale nitter-auth=0
```