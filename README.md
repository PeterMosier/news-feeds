# news-feeds
XML / RSS feeds of various news sources. Home built replacement for "HOURLY NEWS" iOS app (https://apps.apple.com/us/app/hourly-news/id493859859). This formerly excellent app got a much needed update (added speed control, jump back/forward, etc.) but also went to a subscription model (ca$6/mo or ca$60/yr). Without subscribing, users can only choose 2 news sources. I had about six or more news sources in my morning listen routine.

Yes, I know. I could just pay them ca$60/year, but it just seems a little bit much. I would pay CA$10/year, sure. Even ca$20/year, I'd just pay it. But $60 is too much: it's 3X the price of Overcast (currently ca$19.99/year), a general purpose Podcast app (https://apps.apple.com/us/app/overcast-podcast-app/id888422857).

To replace Hourly News, I thought I would be able to simply create a folder in Overcast and add the needed channels. That worked for most (not all) sources that still publish their hourly news via RSS feeds.
- NPR News
- CBC The World This Hour
- DW News
- NPR Marketplace Morning Report
- NPR Marketplace Tech
- NPR Up First
- CNN Five Things
- New York Times Headlines
- New York Times Daily
- WSJ Minute Briefing
- WSJ What's News
- WSJ Tech News Briefing
- WSJ Your Money Briefing
- AP: Headline News from The Associated Press

For balance, I also include some right wing news sources
- Fox News Hourly Update (I like to hear how the fascists are spinning the news)
- Salem Radio News ("newscasts...specifically created for Christian-formatted radio stations") 


## Missing Favourites ##
I was missing two favourites: BBC and FSN, as they don't have RSS feeds for their hourly news summary. More correctly, BBC *no longer* has RSS feeds to deliver their hourly news. Yes, the BBC does syndicate BBC World News via RSS, but that is the hour-long magazine style program; I just want the quick news headlines, like they read every hour on the hour on BBC radio. As for FSN, I think they are a wholesale supplier of news to other organizations; in that case it makes sense that they don't have their own public facing program.

**This GH repo is my attempt to restore those missing news sources.**

## FSN Feature Story News
FSN updates their MP3 at a static URL (https://www.fsnradionews.com/FSNNews/FSNWorldNews.mp3). To capture this MP3 audio and deliver to Overcast, every hour a Github action updates the timestamp and GUID in the RSS/XML stored in this repo so that Overcast recognizes an update has happened and shows that a new episode is available.

Problem: if FSN has not actually updated the MP3 content (e.g. on the weekend there are no updates) the GH Action still updates the RSS/XML with a new timestamp and GUID, and Overcast will incorrectly think there is an update and show a "new" episode is available, even though the MP3 content hasn't changed. For now, I'm willing to live with this glitch.

The following RSS/XML works with Overcast. (Overcast > Magnifying Glass Icon > Add URL)

https://petermosier.github.io/news-feeds/feeds/fsn-world-news.xml

## BBC News
As mentioned above, BBC no longer publishes any easily accessible feeds of their 5 minute news -- they want you to go to the walled-garden of their app. I prefer to have all my news sources together in one curated place, rather than opening "who knows how many" apps. 

The BBC *DOES* have a constant live-stream of their main radio show, and they read news headlines for exactly five minutes at the top of every hour (https://stream.live.vc.bbcmedia.co.uk/bbc_world_service).

Once per hour, at one minute before the top of the hour (xx:59), a Github action in this repo uses FFMPEG to record exactly 8 minutes (480 seconds) of the BBC live stream. The MP3 is stored in the */audio* folder in this repo; no archive is kept and the MP3 file simply gets over-written with the newest recording. Think of it like pressing "Record" on a home cassette deck like we did back in the day, but instead of saving music to a mix tape, I am saving the five-minute news summary to a digital cassette which is constantly overwritten every hour. Then the GH Action updates the timestamp and GUID in the RSS/XML, so that Overcast knows that a new episode is available.

My five minute MP3 (no, you cannot simply jam this into a podcast app!)
https://petermosier.github.io/news-feeds/audio/bbc-latest.mp3

The following XML works with Overcast. (Overcast > Magnifying Glass Icon > Add URL)

https://petermosier.github.io/news-feeds/feeds/bbc-world-news.xml

## cron Problem ##
cron jobs on GH are, apparently, unreliable. They go into a queue with thousands (?) of other jobs and might not run for many  minutes. Somethings those jobs just don't run at all.

## Overcast Update Problem ##
Even when the RSS/XML gets updated (i.e. the cron job ran, eventually) Overcast does not seem to update reliably. That is, even thought the RSS/XML has new date/timestamp, and new GUID, Overcast doesn't indicate a new episode is available.

## To Do: Add the following, One at a time
This is the list of news sources that were/are in the Hourly News app. I may try to add them to the roundup.

- ABC (American Broadcast Corp) Hourly Update (Available on Apple Podcasts and Spotify https://podcasts.apple.com/ca/podcast/abc-news-update/id1314000635?i=1000788361492)
- RTHK News Bulletin
- PMN (Pacific Media Network) Hourly News Updates
- Sky News Bulletin
- Bloomberg News Now
- RNZ (Radio New Zealand) News Bulletin
- 24/7 News: The Latest
- ABC Start Here News
