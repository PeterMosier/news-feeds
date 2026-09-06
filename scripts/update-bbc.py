import datetime
import email.utils
import os

FEED_PATH = "feeds/bbc-world-news.xml"
AUDIO_FILE = "audio/bbc-latest.mp3"

def main():
    # Ensure audio exists
    if not os.path.exists(AUDIO_FILE):
        raise FileNotFoundError(f"Audio file not found: {AUDIO_FILE}")

    # RFC 2822 pubDate (Overcast requires this format)
    pubdate = email.utils.format_datetime(datetime.datetime.utcnow())

    # GUID can be anything unique — timestamp works perfectly
    guid = f"bbc-{int(datetime.datetime.utcnow().timestamp())}"

    # Read existing XML
    with open(FEED_PATH, "r", encoding="utf-8") as f:
        xml = f.read()

    # Replace <pubDate>...</pubDate>
    xml = replace_tag(xml, "pubDate", pubdate)

    # Replace <guid>...</guid>
    xml = replace_tag(xml, "guid", guid)

    # Replace enclosure URL (always the same file)
    xml = replace_enclosure(xml, AUDIO_FILE)

    # Write updated XML
    with open(FEED_PATH, "w", encoding="utf-8") as f:
        f.write(xml)

def replace_tag(xml, tag, new_value):
    """Replace <tag>...</tag> with new_value."""
    start = xml.find(f"<{tag}>")
    end = xml.find(f"</{tag}>", start)
    if start == -1 or end == -1:
        raise ValueError(f"Tag <{tag}> not found in XML.")
    return xml[:start] + f"<{tag}>{new_value}</{tag}>" + xml[end+len(tag)+3:]

def replace_enclosure(xml, audio_path):
    """Replace enclosure URL and length."""
    # Overcast only needs the URL; length is optional
    start = xml.find("enclosure")
    if start == -1:
        raise ValueError("No enclosure tag found.")

    # Build new enclosure tag
    new_tag = (
        f'<enclosure url="{audio_path}" '
        f'type="audio/mpeg" />'
    )

    # Replace entire enclosure tag
    end = xml.find("/>", start)
    return xml[:start] + new_tag + xml[end+2:]

if __name__ == "__main__":
    main()
