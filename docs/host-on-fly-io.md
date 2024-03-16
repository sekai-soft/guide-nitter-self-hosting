### fly.io
Notice: Since this setup exposes the Nitter instance to the Internet, to prevent malicious scrapers, an nginx instance is in front of the Nitter instance with the following protections:

* All RSS paths are protected with a predefined password as a query parameter, e.g. `nitter.net/elonmusk/rss?key=<PREDEFINED PASSWORD>`
* All others paths (except for static resources such as js and css, pictures and videos) are protected with HTTP basic authentication, e.g. when someone goes to a link, they need to enter a predefined username/password combo

1. [Install flyctl on your computer](https://fly.io/docs/hands-on/install-flyctl/)

2. [Sign up and sign in using flyctl](https://fly.io/docs/hands-on/sign-up-sign-in/)

3. Clone my Nitter fork to your computer.
```
git clone https://github.com/sekai-soft/nitter.git && cd nitter
```

4. Create a fly.io app (not deployed yet)
```
flyctl launch --no-deploy
```

When prompted "Would you like to copy its configuration to the new app?", answer `y` (yes)

When prompted "Do you want to tweak these settings before proceeding?", answer `N` (no)

5. Customize your Nitter instance

* **Required:** Burner/temporary Twitter account username

```
flyctl secrets set --detach TWITTER_USERNAME=<your twitter account username>
```

* **Required:** Burner/temporary Twitter account password

```
flyctl secrets set --detach TWITTER_PASSWORD=<your twitter account password>
```

* **Required:** RSS password

```
flyctl secrets set --detach INSTANCE_RSS_PASSWORD=<your rss password>
```

* **Required:** Web UI username

```
flyctl secrets set --detach INSTANCE_WEB_USERNAME=<your web ui username>
```

* **Required:** Web UI password

```
flyctl secrets set --detach INSTANCE_WEB_PASSWORD=<your web ui password>
```

* Optional: Name of your Nitter instance shown on the web UI

```
flyctl secrets set --detach INSTANCE_TITLE=<your instance title>
```

* Optional: Default theme of the web UI. Available options are `Black`, `Dracula`, `Mastodon`, `Nitter`, `Pleroma`, `Twitter` and `Twitter Dark`.

```
flyctl secrets set --detach INSTANCE_TITLE=<your instance default theme>
```

* Optional: Whether to enable infinite scrolling. Enabling this option will load Javascript on the web UI.

```
flyctl secrets set --detach INSTANCE_INFINITE_SCROLL=1
```

6. Deploy the fly.io app
```
flyctl deploy
```

If everything goes well, at the end of the command run, you should see a URL that resembles `https://nitter-SOME-RANDOM-WORDS.fly.dev/`. This URL will be your personal, password-protected Nitter instance!

You should now be able to
* Access your Nitter instance from `https://YOUR-NITTER-INSTANCE-NAME.fly.dev` after you've entered the Web UI username/password combo you entered in step 5
* Access a RSS feed for your Nitter instance such as `https://YOUR-NITTER-INSTANCE-NAME.fly.dev/elonmusk/rss?key=<PASSWORD>`, while `<PASSWORD>` being the RSS password you entered in step 5. You should also be able use this password-suffixed RSS feed in RSS readers or any applications that handle RSS feeds.
