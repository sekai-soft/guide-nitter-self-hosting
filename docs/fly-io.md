Notice: Since deploying to fly.io exposes the Nitter instance to the Internet, to prevent malicious scrapers, an nginx instance is in front of the Nitter instance with the following protections:

* All RSS paths are protected with a predefined password as a query parameter, e.g. `nitter.net/elonmusk/rss?key=<PREDEFINED PASSWORD>`
* All others paths (except for static resources such as js and css, pictures and videos) are protected with HTTP basic authentication, e.g. when someone goes to a link, they need to enter a predefined username/password combo

1. [Install flyctl on your computer](https://fly.io/docs/hands-on/install-flyctl/)

2. [Sign up and sign in using flyctl](https://fly.io/docs/hands-on/sign-up-sign-in/)

3. Create a `nitter` folder and create a `fly.toml` file inside it.
Create an empty `fly.toml` file and paste contents from [this file](https://github.com/sekai-soft/nitter/blob/master/fly.example.toml)

4. Create a fly.io app (not deployed yet)
```
cd nitter && flyctl launch --no-deploy
```

When prompted "Would you like to copy its configuration to the new app?", answer `y` (yes)

When prompted "Do you want to tweak these settings before proceeding?", answer `N` (no)

5. Customize your Nitter instance
In order to customize your Nitter instance, you need to set some environment variables for the fly.io app.

Here is how to set up an environment variable for the fly.io app:

```
flyctl secrets set --detach <environment variable key>=<environment variable value>
```

Here is a list of **required** environment variables for the fly.io app

* `TWITTER_USERNAME`
* `TWITTER_PASSWORD`
* `INSTANCE_RSS_PASSWORD`
* `INSTANCE_WEB_USERNAME`
* `INSTANCE_WEB_PASSWORD`

Consult [this table](https://github.com/sekai-soft/nitter?tab=readme-ov-file#usage) for what each environment variable means and set each one up

For example, to set up `TWITTER_USERNAME`, you would do

```
flyctl secrets set --detach TWITTER_USERNAME=<your twitter account username>
```

[The table](https://github.com/sekai-soft/nitter?tab=readme-ov-file#usage) also contains several customization options such as instance title and instance default theme that you might be interested in.

6. Deploy the fly.io app
```
flyctl deploy
```

If everything goes well, at the end of the command run, you should see a URL that resembles `https://nitter-SOME-RANDOM-WORDS.fly.dev/`. This URL will be your personal, password-protected Nitter instance!

You should now be able to
* Access your Nitter instance from `https://YOUR-NITTER-INSTANCE-NAME.fly.dev` after you've entered the Web UI username/password combo you entered in step 5
* Access a RSS feed for your Nitter instance such as `https://YOUR-NITTER-INSTANCE-NAME.fly.dev/elonmusk/rss?key=<PASSWORD>`, while `<PASSWORD>` being the RSS password you entered in step 5. You should also be able use this password-suffixed RSS feed in RSS readers or any applications that handle RSS feeds.
