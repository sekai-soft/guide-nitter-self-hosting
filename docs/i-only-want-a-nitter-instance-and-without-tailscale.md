### I only want a Nitter instance and without Tailscale
Notice: Since this setup could potentially expose the Nitter instance to the Internet, to prevent malicious scrapers, an nginx instance is in front of the Nitter instance with the following protections:

* All RSS paths are protected with a predefined key/password as a query parameter, e.g. `nitter.net/elonmusk/rss?key=<PREDEFINED PASSWORD>`
* All others paths (except for static resources such as js and css, pictures and videos) are protected with HTTP basic authentication, e.g. when someone goes to a link, they need to enter a predefined username/password combo

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

4. Create a `.htpasswd` file
Go to a website (I used https://iplocation.io/htaccess-secure-directory) or use the `htpasswd` CLI to generate a `.htpasswd` file under this directory.

5. Customize your nginx configuration
```
cp nitter-guardian.nginx.example.conf nitter-guardian.nginx.conf
```
**Be sure to replace `RSS_PASSWORD` in your `nitter-guardian.nginx.conf` with your own. This will be the password to your Nitter instance's RSS feeds**

6. Run this command to run the services
```
docker compose -f docker-compose.nitter.yml up -d --scale nitter-auth=0
```
If everything goes well, you should now be able to
* Access your Nitter instance from `http://localhost:8080` after you've entered the username/password combo you used to generate `.htpasswd` in step 4.
* Access a RSS feed for your Nitter instance such as `http://localhost:8080/elonmusk/rss?key=<PASSWORD>`, while `<PASSWORD>` being the `RSS_PASSWORD` you specified in step 5. You should also be able use this password-suffixed RSS feed in RSS readers or any applications that handle RSS feeds.
