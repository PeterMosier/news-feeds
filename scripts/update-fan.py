import datetime
from email.utils import format_datetime

FEED_PATH = "feeds/fsn-world-news.xml"

# Generate new timestamp + GUID
now = datetime.datetime.utcnow()
pubdate = format_datetime(now)
guid = f"fsn-world-news-{now.strftime('%Y%m%d-%H%M')}"

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

# Write updated XML
with open(FEED_PATH, "w", encoding="utf-8") as f:
    f.write(xml)

print("Updated FSN feed.")
