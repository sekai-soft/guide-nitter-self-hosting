### I want a Nitter instance for RSS reading in Tailscale
1. You need to setup Tailscale
    1. [Sign up](https://login.tailscale.com/start) for a Tailscale account if you haven't already
    2. Tailscale clients are installed on devices that you want to access Nitter and miniflux with. Install from [here](https://tailscale.com/download).
    3. Create a Tailscale auth-key from [here](https://login.tailscale.com/admin/settings/keys). Use the following configurations
        * Description: <put anything that's identifiable to you>
        * Reusable: yes
        * Expiration: 90 days
        * Ephemeral: No
        * Tags: <if you know what tags are used for, you probably know what tags to use, otherwise just leave it empty :)>
    4. Make sure MagicDNS is enabled [here](https://login.tailscale.com/admin/dns)

2. Clone this repo on your NAS/server.
```
git clone https://github.com/sekai-soft/guide-nitter-self-hosting && cd guide-nitter-self-hosting
```

3. Run this command to obtain credentials for your **burner/temporary** Twitter account
```
docker compose run --build nitter-auth
```
At the end of the command run, follow instructions "In terminal, run the following command"

4. Create a `.env` file
```
cp .example.env .env
```
On the `.env` file, fill in

* TS_AUTHKEY=<the Tailscale auth-key you obtained from step 1.3>

Optionally, if you want crossposting from Twitter to Mastodon, follow [this guide](https://github.com/k-t-corp/nitter-xposter?tab=readme-ov-file#obtain-mastodon-credentials) to fill in the rest of `.env` file

5. Customize your Nitter instance
```
cp nitter.example.conf nitter.conf
```
Some customizations you can make to your Nitter instance in the `nitter.conf` file
* `title`: Name of your Nitter instance shown on the web UI
* `theme`: Default theme of the web UI. Available options are `Black`, `Dracula`, `Mastodon`, `Nitter`, `Pleroma`, `Twitter` and `Twitter Dark`.
* `infiniteScroll`: Whether to enable infinite scrolling. Enabling this option will load Javascript on the web UI.

6. Run this command to run the services
```
docker compose up -d --scale nitter-auth=0 --scale nitter-xposter=0 --scale nitter-xposter-bsky=0
```
If everything goes well, you should now be able to
* Access your private Nitter instance from `http://nitter` on devices that have Tailscale client installed
* Access your private miniflux instance from `http://miniflux` on devices that have Tailscale client installed
    * In your miniflux interface, you can follow Twitter accounts as RSS feeds using the URL `http://nitter/<twitter handle>/rss`
