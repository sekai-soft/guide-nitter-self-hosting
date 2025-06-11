# A guide for self-hosting a Nitter instance

## Why
[Nitter](https://github.com/zedeus/nitter) is a fantastic alternative frontend for Twitter. Instead of using Twitter's official web interface or app, which contains ads or algorithmic contents that you may not like, Nitter enables you to **browse** Twitter content without those potential distractions. Nitter also exposes Twitter contents as RSS feeds so that you can 1) view them in an RSS reader 2) manipulate them programatically, such as crossposting to Mastodon, filtering and archiving.

If this sounds interesting to you, read on.

There were once [public Nitter instances](https://github.com/zedeus/nitter/wiki/Instances) that you can just use. However, with some [recent changes happening on Twitter's side](https://github.com/zedeus/nitter/issues/983), it's becoming increasingly hard for people to host public Nitter instances.

However, regardless of the demise of public Nitter instances, it is still possible to use Nitter as long as you host your own instance and use it on a personal scale only, and this is a guide that helps you do exactly that.

## What do you need
* A **burner/temporary** Twitter account **without 2FA enabled** (sign up [here](https://twitter.com/i/flow/signup))
* Some Linux and terminal knowledge

## Steps to host on a server or NAS
### 1. Create a `docker-compose.yml` file.
Create a `docker-compose.yml` file by copying [this file](https://github.com/sekai-soft/guide-nitter-self-hosting/blob/master/docker-compose.yml)

### 2. Create a `.env` file
Create an empty `.env` file

Fill in the `.env` file by writing `<ENVIRONMENT_VARIABLE_NAME>=<ENVIRONMENT_VARIABLE_VALUE>`, e.g. `INSTANCE_RSS_PASSWORD=123`

If you are hosting the Nitter instance on the public Internet, e.g. a public VPS server, you may want to protect it with credentials to prevent malicious scrapers. Continue to "Fill in instance credentials" section.

If you are not hosting the Nitter instance on the public Internet and don't care about protecting against malicious scrapers, continue to "Disable instance protection" section

#### Fill in instance credentials

* All RSS paths will be protected with a predefined password as a query parameter, e.g. `nitter.net/elonmusk/rss?key=<PREDEFINED PASSWORD>`
* All others paths (except for static resources such as js and css, pictures and videos) will be protected with HTTP basic authentication, e.g. when someone goes to a link, they need to enter a predefined username/password combo

Fill in those environment variables

* `INSTANCE_RSS_PASSWORD`
* `INSTANCE_WEB_USERNAME`
* `INSTANCE_WEB_PASSWORD`

Consult [this table](https://github.com/sekai-soft/nitter?tab=readme-ov-file#usage) for what each environment variable means and fill in each one

#### Disable instance protection

* Change the line `"0.0.0.0:8080:8081"` to `"0.0.0.0:8080:8080"`
* Add environment variable `DISABLE_NGINX=1`

### 3. Provide Twitter credentials
1. Create a `twitter-credentials.json` file by copying [this file](https://github.com/sekai-soft/guide-nitter-self-hosting/blob/master/twitter-credentials.example.json)

2. Fill in the `twitter-credentials.json` file with username and passwords. The example has only two accounts but you can of course add as many as you want.

### 4. (Optional) Customize the Nitter instance

[This table](https://github.com/sekai-soft/nitter?tab=readme-ov-file#usage) also contains several customization options such as instance title and instance default theme that you might be interested in

Simply add the relevant environment variables to the `.env` file

Optionally, you can also pass in custom `nitter.conf`. In the `docker-compose.yml` file, uncomment the two lines `- ./nitter.conf:/src/nitter.conf` and `- USE_CUSTOM_CONF=1`

### 5. Run the services
```
docker compose up -d
```
If everything goes well, you should now be able to
* Access your Nitter instance from `http://localhost:8080` after you've entered the Web UI username/password combo you used in step 2.
* Access a RSS feed for your Nitter instance such as `http://localhost:8080/elonmusk/rss?key=<PASSWORD>`, while `<PASSWORD>` being the RSS password you specified in step 2. You should also be able use this password-suffixed RSS feed in RSS readers or any applications that handle RSS feeds.
