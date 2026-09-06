# news-feeds
XML / RSS feeds of various news sources. Home built replacement for "NEWS" iOS app. This formerly excellent app got a much needed update (added speed control, etc.) but also went to a subscription model ($6/mo or $60/yr). Without subscribing, users can only choose 2 news sources.

I thought I would be able to simply create a folder in Overcast (Podcast app) and add the needed channels, but that only worked for some (NPR, Faux News, DW News, NPR Marketplace Morning Report, NPR Marketplace Tech). 

But I was missing CBC, BBC, FSN.

So this GH repo is my attempt to restore those missing news sources.

## FSN Feature Story News
FSN updates an MP3 at a static address (https://www.fsnradionews.com/FSNNews/FSNWorldNews.mp3). Every hour a Github action updates the timestamp and GUID in the RSS/XML so that Overcast recognizes and update. Problem: if FSN has not actually updated the MP3 (e.g. on the weekend) then Overcast will incorrectly think there is an update.

The following XML works with Overcast.
https://petermosier.github.io/news-feeds/feeds/fsn-world-news.xml

## BBC News
BBC no longer publishes any easily accessible feeds of their 5 minute news -- they want you to go to the walled-garden of their app. I prefer to have all my news sources together in one place.

Once per hour, at the top of the hour, a Github action uses FFMPEG to record exactly 5 minutes of the BBC live stream (https://stream.live.vc.bbcmedia.co.uk/bbc_world_service). Then the GH Action updates the timestamp and GUID in the RSS/XML.

The following XML works with Overcast.
https://petermosier.github.io/news-feeds/feeds/bbc-world-news.xml

## To Do: CBC Radio News
One at a time. This is next.
