# news-feeds
XML / RSS feeds of various news sources. Home built replacement for "NEWS" iOS app

Add the URLs below to Podcast app (Overcast, etc.) 

## FSN Feature Story News RSS/XML URL
FSN updates an MP3 at a static address ().
https://petermosier.github.io/news-feeds/feeds/fsn-world-news.xml

## BBC News
Once per hour, at the top of the hour, a Github action uses FFMPEG to record exactly 5 minutes of the BBC live stream (https://stream.live.vc.bbcmedia.co.uk/bbc_world_service). Then the GH Action updates the timestamp and GUID in the RSS/XML.

The following XML works with Overcast.
https://petermosier.github.io/news-feeds/feeds/bbc-world-news.xml

## More to follow
