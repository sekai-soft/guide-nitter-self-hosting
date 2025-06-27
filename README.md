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
Create a `docker-compose.yml` file by copying [this file](https://github.com/zedeus/nitter/blob/master/docker-compose.yml)

Replace `zedeus/nitter:latest` with `zedeus/nitter:latest-arm64` if your server or NAS is ARM64

### 2. Create a `nitter.conf` file
Create a `nitter.conf` file by copying [this file](https://github.com/zedeus/nitter/blob/master/nitter.example.conf)

Change `redisHost = "localhost"` to `redisHost = "nitter-redis"`

Customize other options of this config file to your liking

### 3. Obtain credentials
Clone [Nitter repo](https://github.com/zedeus/nitter)

In the repo, run

```
pushd tools
pip3 install pyotp requests
python3 get_session.py <burner twitter account username> <burner twitter account password> <2fa secret; put 000000 if 2fa is disabled> ../sessions.jsonl
popd
```

Place the resulting `sessions.jsonl` to the directory you were working in from the previous step

### 4. Run Nitter
```
docker compose up -d
```
If everything goes well, you should now be able to
* Access your Nitter instance from `http://localhost:8080`
* Access a RSS feed for your Nitter instance such as `http://localhost:8080/elonmusk/rss`
