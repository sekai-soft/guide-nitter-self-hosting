### I only want a Nitter instance for crossposting
1. Clone this repo on your NAS/server.
```
git clone https://github.com/sekai-soft/guide-nitter-self-hosting && cd guide-nitter-self-hosting
```

2. Run this command to obtain credentials for your **burner/temporary** Twitter account
```
docker compose run --build nitter-auth
```
At the end of the command run, follow instructions "In terminal, run the following command"

3. Create a configuration file for your Nitter instance
```
cp nitter.example.conf nitter.conf
```

4. Create a `.env` file
```
cp .example.env .env
```
Follow [this guide](https://github.com/k-t-corp/nitter-xposter?tab=readme-ov-file#usage) to fill in the .env file

* In the `environment` sections mentioned in the guide, treat each item as a `KEY=<VALUE>` line in the .env file
* You can omit either Mastodon or Bluesky if you only want to crosspost to one of them

5. Run this command to start crossposting to both Mastodon and Bluesky
```
docker compose -f docker-compose.nitter-xposter.yml up -d --scale nitter-auth=0
```

To crosspost to only Mastodon, run
```
docker compose -f docker-compose.nitter-xposter.yml up -d --scale nitter-auth=0 --scale nitter-xposter-bsky=0
```

To crosspost to only Bluesky, run
```
docker compose -f docker-compose.nitter-xposter.yml up -d --scale nitter-auth=0 --scale nitter-xposter=0
```

To verify that this works, run
```
docker compose -f docker-compose.nitter-xposter.yml logs
```
to see logs emitted from `nitter-xposter`
