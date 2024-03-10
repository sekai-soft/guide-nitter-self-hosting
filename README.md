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

## How-to's
Depending on what you specific components you want from the `What can you expect` section...

* [I want everything! (without crossposting)](./docs/i-want-everything-without-crossposting.md)
* [I only want a Nitter instance and without Tailscale](./docs/i-only-want-a-nitter-instance-and-without-tailscale.md)
* [I only want a Nitter instance and a nitter-xposter instance without Tailscale](#i-only-want-a-nitter-instance-and-a-nitter-xposter-instance-without-tailscale)

## Like what you see?
Consider support us on [Patreon](https://www.patreon.com/sekaisoft) :)
