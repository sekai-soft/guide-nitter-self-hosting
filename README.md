# FreeBird
A guide for self-hosting a Nitter instance & additional accessories

## Why
I want to view latest tweets from a bunch of Twitter accounts

but without using my main Twitter account (because of privacy concerns)

and without using the Twitter app (because I don't like the Twitter app interface for one reason or another)

If this sounds like you, read on

## What can you expect
* A [Nitter](https://github.com/zedeus/nitter) instance ([a working one](https://github.com/zedeus/nitter/issues/983))
    * Notice that only 1) viewing profiles and 2) view individual tweets are confirmed to be working. Other pages on the Nitter web interface such as searching are NOT guaranteed to work.
* A [miniflux](https://github.com/miniflux/v2) instance that can poll Twitter accounts from the Nitter instance as RSS feeds
    * Depending on the volume of Twitter accounts that you want to follow, the miniflux instance may not be able to poll the absolutely latest tweet timely.
    * A custom polling scheduler for Miniflux is included so that instead of polling all accounts all at once and causing the Nitter instance to be rate-limited, Twitter accounts are polled one by one and with random time intervals in between.
* A [rss-lambda](https://github.com/k-t-corp/rss-lambda) instance that you can use to perform operations such as filter by keyword on RSS feeds.
* Everything is provisioned in a [Tailscale](https://tailscale.com/) private network so that you can access Nitter and miniflux (even via a third-party RSS reader) **without exposing them to the Internet** and on the go.
* Optionally, you can also have just a [Nitter](https://github.com/zedeus/nitter) instance and a [nitter-xposter](https://github.com/k-t-corp/nitter-xposter) instance that you can use to crosspost from (public) Twitter accounts to Mastodon and Bluesky accounts

## What do you need
* A **burner/temporary** Twitter account **without 2FA enabled** (sign up [here](https://twitter.com/i/flow/signup))
* A **home** NAS or server running Linux on x86_64 with Docker installed
    * A cloud VPS may work but NOT guaranteed, depending on whether the IP will be blocked. A home IP is probably a safer bet.
* If you understand the above you probably know some Linux and terminal stuff as well :)

## How-to
Depending on what you specific components you want from the `What can you expect` section...

[I want everything! (without crossposting)](#i-want-everything-without-crossposting)

[I only want a Nitter instance and without Tailscale](#i-only-want-a-nitter-instance-and-without-tailscale)

[I only want a Nitter instance and a nitter-xposter instance without Tailscale](#i-only-want-a-nitter-instance-and-a-nitter-xposter-instance-without-tailscale)

### I want everything! (without crossposting)
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
git clone https://github.com/sekai-soft/freebird && cd freebird
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

### I only want a Nitter instance and without Tailscale
Notice: since I personally do not use this configuration, it may get bug fixes and improvements slower than the "I want everything!" configuration.

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

### I only want a Nitter instance and a nitter-xposter instance without Tailscale
1. Clone this repo on your NAS/server.
```
git clone https://github.com/sekai-soft/freebird && cd freebird
```

2. Run this command to obtain credentials for your **burner/temporary** Twitter account
```
docker compose run --build nitter-auth
```
At the end of the command run, follow instructions "In terminal, run the following command"

3. Create a configuration file for your Nitter instance
```
cp nitter.example.conf nitter.conf
```

4. Create a `.env` file
```
cp .example.env .env
```
Follow [this guide](https://github.com/k-t-corp/nitter-xposter?tab=readme-ov-file#usage) to fill in the .env file

* In the `environment` sections mentioned in the guide, treat each item as a `KEY=<VALUE>` line in the .env file
* You can omit either Mastodon or Bluesky if you only want to crosspost to one of them

5. Run this command to start crossposting to both Mastodon and Bluesky
```
docker compose -f docker-compose.nitter-xposter.yml up -d --scale nitter-auth=0
```

To crosspost to only Mastodon, run
```
docker compose -f docker-compose.nitter-xposter.yml up -d --scale nitter-auth=0 --scale nitter-xposter-bsky=0
```

To crosspost to only Bluesky, run
```
docker compose -f docker-compose.nitter-xposter.yml up -d --scale nitter-auth=0 --scale nitter-xposter=0
```

To verify that this works, run
```
docker compose -f docker-compose.nitter-xposter.yml logs
```
to see logs emitted from `nitter-xposter`

## Like what you see?
Consider support us on [Patreon](https://www.patreon.com/sekaisoft) :)
