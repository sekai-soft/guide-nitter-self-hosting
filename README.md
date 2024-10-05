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

[Guide](./docs/fly-io.md)

## Host on a server or NAS
You need a server or NAS running Linux on x86_64 or arm64 with Docker installed (verify by running `docker run hello-world` and `docker compose -v` if you are unsure)

[Guide](./docs/server.md)

## TODO
- [x] An integrated docker entrypoint that handles all the credential retrieving, Nitter configuration, nginx configuration, etc., so that one can just start the Docker container/fly.io app with environment variables and start using the instance, instead of fiddling in a terminal
- [ ] An bootstrapping and admin UI
- [ ] Deploy to Zeabur
- [ ] Deploy to Railway
- [ ] Deploy to Vercel
