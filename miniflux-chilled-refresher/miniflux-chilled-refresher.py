import os
import time
import random
import logging
import miniflux
import requests

logging.basicConfig(
    format='%(asctime)s %(levelname)-8s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S')

miniflux_url = os.getenv("REFRESHER_MINIFLUX_URL", "http://miniflux")
miniflux_username = os.getenv("REFRESHER_MINIFLUX_USERNAME", "admin")
miniflux_password = os.getenv("REFRESHER_MINIFLUX_PASSWORD", "test123")
client = miniflux.Client(miniflux_url, username=miniflux_username, password=miniflux_password)

refresh_interval_seconds = int(os.getenv("REFRESHER_REFRESH_INTERVAL_SECONDS", "60"))
hearbeat_url = os.getenv("REFRESHER_HEARTBEAT_URL")

while True:
    feeds = client.get_feeds()
    for feed in feeds:
        logging.info(f"Refreshing {feed['feed_url']}")
        try:
            client.refresh_feed(feed['id'])
        except miniflux.ClientError as e:
            logging.error(f"Error refreshing {feed['feed_url']} but continuing: {e}")
        feed_sleep_seconds = refresh_interval_seconds + random.randint(1, refresh_interval_seconds)
        logging.info(f"Feed sleeping for {feed_sleep_seconds} seconds")
        time.sleep(feed_sleep_seconds)
        if hearbeat_url:
            try:
                requests.get(hearbeat_url)
            except Exception as e:
                logging.error(f"Error sending heartbeat but continuing: {e}")
    loop_sleep_seconds = refresh_interval_seconds * len(feeds) * 2
    logging.info(f"Loop sleeping for {loop_sleep_seconds}; there were {len(feeds)} feeds")
    time.sleep(loop_sleep_seconds)
