### I only want a Nitter instance and without Tailscale
Notice: Since this setup exposes the Nitter instance on port 8080, depending on your Docker/host/firewall setup, the instance could be exposed to the Internet and be abused by scapers.

If you choose to use this setup, make sure that you either 1) set it up in your home NAS/server where you know scrapers on the Internet cannot access, or 2) set up some kind of rate-limit mechanism such as `fail2ban` if the instance is hosted on a VPS.

1. Clone this repo on your NAS/server.
```
git clone https://github.com/sekai-soft/freebird && cd freebird
```

2. Run this command to obtain credentials for your **burner/temporary** Twitter account
```
docker compose run --build nitter-auth
```
At the end of the command run, follow instructions "In terminal, run the following command"

3. Customize your Nitter instance
```
cp nitter.example.conf nitter.conf
```
Some customizations you can make to your Nitter instance in the `nitter.conf` file
* `title`: Name of your Nitter instance shown on the web UI
* `theme`: Default theme of the web UI. Available options are `Black`, `Dracula`, `Mastodon`, `Nitter`, `Pleroma`, `Twitter` and `Twitter Dark`.
* `infiniteScroll`: Whether to enable infinite scrolling. Enabling this option will load Javascript on the web UI.

4. Run this command to run the services
```
docker compose -f docker-compose.nitter.yml up -d --scale nitter-auth=0
```
If everything goes well, you should now be able to
* Access your Nitter instance from `http://localhost:8080`
