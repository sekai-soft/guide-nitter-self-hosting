# A guide for self-hosting a Nitter instance

## Why
[Nitter](https://github.com/zedeus/nitter) is a fantastic alternative frontend for Twitter. Instead of using Twitter's official web interface or app, which contains ads or algorithmic contents that you may not like, Nitter enables you to **browse** Twitter content without those potential distractions. Nitter also exposes Twitter contents as RSS feeds so that you can 1) view them in an RSS reader 2) manipulate them programatically, such as crossposting to Mastodon, filtering and archiving.

If this sounds interesting to you, read on.

There were once [public Nitter instances](https://github.com/zedeus/nitter/wiki/Instances) that you can just use. However, with some [recent changes happening on Twitter's side](https://github.com/zedeus/nitter/issues/983), it's becoming increasingly hard for people to host public Nitter instances.

However, regardless of the demise of public Nitter instances, it is still possible to use Nitter as long as you host your own instance and use it on a personal scale only, and this is a guide that helps you do exactly that.

## What do you need
* A **burner/temporary** Twitter account **without 2FA enabled** (sign up [here](https://twitter.com/i/flow/signup))
* Some Linux and terminal knowledge

## Decide where to host the Nitter instance
* [fly.io, a Platform-as-a-Service hosting provider](https://fly.io/) -> [go to the "Host on fly.io" section](#host-on-flyio)
* A server or NAS -> [go to the "Host on a server or NAS" section](#host-on-a-server-or-nas)

## Host on fly.io
With the fly.io setup, you will get a personal, password-protected Nitter instance on the Internet.

Although fly.io is a paid platform, the setup uses as minimal as possible resources and your usage should fall into their free tier as long as you keep it just for personal usage.

[Guide](https://github.com/sekai-soft/nitter/blob/master/docs/host-on-fly-io.md)

## Host on a server or NAS
You need a server or NAS running Linux on x86_64 or arm64 with Docker installed (verify by running `docker run hello-world` and `docker compose -v` if you are unsure)

You have a choice between three use cases

* [I only want a Nitter instance](./docs/i-only-want-a-nitter-instance.md)
* [I only want a Nitter instance for crossposting](./docs/i-only-want-a-nitter-instance-for-crossposting.md)
* [I want a Nitter instance for RSS reading in Tailscale](./docs/i-want-a-nitter-instance-for-rss-reading-in-tailscale.md)
    * Notice that this setup contains a few extra things in addition to the bare minimal Nitter instance for RSS reading in a Tailscale private network.
        * A [miniflux](https://github.com/miniflux/v2) instance that can poll Twitter accounts from the Nitter instance as RSS feeds
            * Depending on the volume of Twitter accounts that you want to follow, the miniflux instance may not be able to poll the absolutely latest tweet timely.
            * A custom polling scheduler for Miniflux is included so that instead of polling all accounts all at once and causing the Nitter instance to be rate-limited, Twitter accounts are polled one by one and with random time intervals in between.
        * A [rss-lambda](https://github.com/k-t-corp/rss-lambda) instance that you can use to perform operations such as filter by keyword on RSS feeds.
        * Everything in this setup is provisioned in a [Tailscale](https://tailscale.com/) private network so that you can access Nitter and miniflux (even via a third-party RSS reader) without exposing them to the Internet and on the go.

## Potential new stuff
- [ ] Other PaaS such as Railway, Zeit, PikaPod.
- [ ] An integrated docker entrypoint that handles all the credential retrieving, Nitter configuration, nginx configuration, etc., so that one can just start the Docker container/fly.io app with environment variables and start using the instance, instead of fiddling in a terminal.

## Like what you see?
Consider support us on [Patreon](https://www.patreon.com/sekaisoft) :)
