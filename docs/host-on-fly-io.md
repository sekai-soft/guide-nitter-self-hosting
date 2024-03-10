### fly.io
Notice: Since this setup exposes the Nitter instance to the Internet, to prevent malicious scrapers, an nginx instance is in front of the Nitter instance with the following protections:

* All RSS paths are protected with a predefined password as a query parameter, e.g. `nitter.net/elonmusk/rss?key=<PREDEFINED PASSWORD>`
* All others paths (except for static resources such as js and css, pictures and videos) are protected with HTTP basic authentication, e.g. when someone goes to a link, they need to enter a predefined username/password combo

1. [Install flyctl on your computer](https://fly.io/docs/hands-on/install-flyctl/)

2. [Sign up and sign in using flyctl](https://fly.io/docs/hands-on/sign-up-sign-in/)

3. Clone this repo to your computer.
```
git clone https://github.com/sekai-soft/freebird && cd freebird
```

4. Run this command to obtain credentials for your **burner/temporary** Twitter account
```
docker compose run --build nitter-auth
```
At the end of the command run, follow instructions "In terminal, run the following command"

5. Clone my Nitter fork to your computer.
```
cd .. && git clone https://github.com/sekai-soft/nitter.git && cd nitter
```

6. Copy over the Twitter credentials
```
cp ../freebird/nitter-guest_accounts.json guest_accounts.json
```

7. Customize your Nitter instance
```
cp nitter.example.conf fly.nitter.conf
```
Some customizations you can make to your Nitter instance in the `fly.nitter.conf` file
* `title`: Name of your Nitter instance shown on the web UI
* `theme`: Default theme of the web UI. Available options are `Black`, `Dracula`, `Mastodon`, `Nitter`, `Pleroma`, `Twitter` and `Twitter Dark`.
* `infiniteScroll`: Whether to enable infinite scrolling. Enabling this option will load Javascript on the web UI.

8. Create a `.htpasswd` file

Go to a website (I used https://iplocation.io/htaccess-secure-directory) or use the `htpasswd` CLI to generate a `.htpasswd` file under this directory. **This will be the username/password combo that protects the web interfaces of the Nitter instance.**

The resulting `.htpasswd` file's content should look something like

```
username:$apr1$somehash...
```

9. Customize your nginx configuration
```
cp fly.nginx-site.example.conf fly.nginx-site.conf
```
**Be sure to replace `RSS_PASSWORD` in your `fly.nginx-site.conf` with your own. This will be the password that proteced RSS feeds of the Nitter instance.**

10. Run this command to launch the instance on fly.io
```
flyctl launch
```
When prompted "Would you like to copy its configuration to the new app?", answer `y` (yes)

When prompted "Do you want to tweak these settings before proceeding?", answer `N` (no)

If everything goes well, at the end of the command run, you should see a URL that resembles `nitter-SOME-RANDOM-WORDS.fly.dev`. This URL will be your personal, password-protected Nitter instance!

You should now be able to
* Access your Nitter instance from `https://YOUR-NITTER-INSTANCE-NAME.fly.dev` after you've entered the username/password combo you used to generate `.htpasswd` in step 8.
* Access a RSS feed for your Nitter instance such as `https://YOUR-NITTER-INSTANCE-NAME.fly.dev/elonmusk/rss?key=<PASSWORD>`, while `<PASSWORD>` being the `RSS_PASSWORD` you specified in step 9. You should also be able use this password-suffixed RSS feed in RSS readers or any applications that handle RSS feeds.
