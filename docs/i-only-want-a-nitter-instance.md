### I only want a Nitter instance
Notice: Since this setup could potentially expose the Nitter instance to the Internet, to prevent malicious scrapers, an nginx instance is in front of the Nitter instance with the following protections:

* All RSS paths are protected with a predefined password as a query parameter, e.g. `nitter.net/elonmusk/rss?key=<PREDEFINED PASSWORD>`
* All others paths (except for static resources such as js and css, pictures and videos) are protected with HTTP basic authentication, e.g. when someone goes to a link, they need to enter a predefined username/password combo

1. Clone repo on your NAS/server.
```
git clone https://github.com/sekai-soft/guide-nitter-self-hosting && cd guide-nitter-self-hosting
```

2. Make neccessary and optional configuration changes
```
cp nitter.example.conf nitter.conf
```
Fill in the `.env` file
* **(Required)** `TWITTER_USERNAME`: Burner/temporary Twitter account username
* **(Required)** `TWITTER_PASSWORD`: Burner/temporary Twitter account password
* **(Required)** `INSTANCE_RSS_PASSWORD`: RSS password
* **(Required)** `INSTANCE_WEB_USERNAME`: Web UI username
* **(Required)** `INSTANCE_WEB_PASSWORD`: Web UI password
* Optional `INSTANCE_TITLE`: Name of your Nitter instance shown on the web UI
* Optional `INSTANCE_THEME`: Default theme of the web UI. Available options are `Black`, `Dracula`, `Mastodon`, `Nitter`, `Pleroma`, `Twitter` and `Twitter Dark`.
* Optional `INSTANCE_INFINITE_SCROLL`: Whether to enable infinite scrolling. Enabling this option will load Javascript on the web UI. Set it to `1` to enable.
* Optional `INSTANCE_HOSTNAME`: The hostname used to render public-facing URLs such as hyperlinks in RSS feeds.

3. Run the services
```
docker compose -f docker-compose.nitter.yml up -d
```
If everything goes well, you should now be able to
* Access your Nitter instance from `http://localhost:8080` after you've entered the Web UI username/password combo you used in step 2.
* Access a RSS feed for your Nitter instance such as `http://localhost:8080/elonmusk/rss?key=<PASSWORD>`, while `<PASSWORD>` being the RSS password you specified in step 2. You should also be able use this password-suffixed RSS feed in RSS readers or any applications that handle RSS feeds.
