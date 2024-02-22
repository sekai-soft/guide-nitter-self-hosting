import time
import random
import logging
import miniflux

logging.basicConfig(
    format='%(asctime)s %(levelname)-8s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S')

# Creating a client using username / password authentication
client = miniflux.Client("http://miniflux", username="admin", password="test123")

refresh_interval_seconds = 60

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
    loop_sleep_seconds = refresh_interval_seconds * len(feeds) * 2
    logging.info(f"Loop sleeping for {loop_sleep_seconds}; there were {len(feeds)} feeds")
    time.sleep(loop_sleep_seconds)
