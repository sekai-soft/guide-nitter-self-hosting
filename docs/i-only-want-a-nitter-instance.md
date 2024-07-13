### I only want a Nitter instance
Notice: Since this setup could potentially expose the Nitter instance to the Internet, to prevent malicious scrapers, an nginx instance is in front of the Nitter instance with the following protections:

* All RSS paths are protected with a predefined password as a query parameter, e.g. `nitter.net/elonmusk/rss?key=<PREDEFINED PASSWORD>`
* All others paths (except for static resources such as js and css, pictures and videos) are protected with HTTP basic authentication, e.g. when someone goes to a link, they need to enter a predefined username/password combo

1. Clone repo on your NAS/server.
```
git clone https://github.com/sekai-soft/guide-nitter-self-hosting && cd guide-nitter-self-hosting
```

Fill in the `.env` file

Here is a list of **required** environment variables

* `TWITTER_USERNAME`
* `TWITTER_PASSWORD`
* `INSTANCE_RSS_PASSWORD`
* `INSTANCE_WEB_USERNAME`
* `INSTANCE_WEB_PASSWORD`

Consult [this table](https://github.com/sekai-soft/nitter/blob/master/docs/self-contained-docker-image.md#how-to-use) for what each environment variable means and fill in each one

[The table](https://github.com/sekai-soft/nitter/blob/master/docs/self-contained-docker-image.md#how-to-use) also contains several customization options such as instance title and instance default theme that you might be interested in.

2. Run the services
```
docker compose -f docker-compose.nitter.yml up -d
```
If everything goes well, you should now be able to
* Access your Nitter instance from `http://localhost:8080` after you've entered the Web UI username/password combo you used in step 2.
* Access a RSS feed for your Nitter instance such as `http://localhost:8080/elonmusk/rss?key=<PASSWORD>`, while `<PASSWORD>` being the RSS password you specified in step 2. You should also be able use this password-suffixed RSS feed in RSS readers or any applications that handle RSS feeds.
