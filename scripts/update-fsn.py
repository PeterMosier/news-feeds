import datetime
from email.utils import format_datetime

FEED_PATH = "feeds/fsn-world-news.xml"

# Generate new timestamp + GUID
now = datetime.datetime.utcnow()
pubdate = format_datetime(now)
guid = f"fsn-world-news-{now.strftime('%Y%m%d-%H%M')}"
title = f"FSN World News — {now.strftime('%Y-%m-%d %H:%M UTC')}"

# Cache-busting timestamp for enclosure URL
ts = int(now.timestamp())
enclosure_url = f"https://petermosier.github.io/news-feeds/audio/fsn-latest.mp3?ts={ts}"


# Read XML
with open(FEED_PATH, "r", encoding="utf-8") as f:
    xml = f.read()

# Replace pubDate
import re
xml = re.sub(r"<pubDate>.*?</pubDate>",
             f"<pubDate>{pubdate}</pubDate>",
             xml)

# Replace GUID
xml = re.sub(r"<guid.*?>.*?</guid>",
             f'<guid isPermaLink="false">{guid}</guid>',
             xml)

# Replace episode title inside <item>
xml = re.sub(
    r"<item>.*?<title>.*?</title>",
    lambda m: re.sub(
        r"<title>.*?</title>",
        f"<title>{title}</title>",
        m.group(0)
    ),
    xml,
    flags=re.DOTALL
)

# Replace enclosure URL (with timestamp)
xml = re.sub(
    r'<enclosure[^>]*>',
    f'<enclosure url="{enclosure_url}" type="audio/mpeg" />',
    xml
)


# Write updated XML
with open(FEED_PATH, "w", encoding="utf-8") as f:
    f.write(xml)

print("Updated FSN feed.")
