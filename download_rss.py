# import all the shit
import requests
import feedparser
import re
from RSS_Sources import RSS_FEED_LIST

# do the things
print(RSS_FEED_LIST['Pauls_Hardware'])
print('\r\n')

# feed_content = feedparser.parse(RSS_FEED_LIST['Pauls_Hardware']).keys()
# feed_content_str = str(feed_content)

RSS_CONTENT = requests.get(RSS_FEED_LIST['Pauls_Hardware'])
RSS_CONTENT_STR = str(RSS_CONTENT.content)
print(RSS_CONTENT.status_code)

# print(RSS_CONTENT_STR)
URL_REGEX =  "https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()!@:%_\+.~#?&\/\/=]*)"

URLS = re.findall(URL_REGEX, RSS_CONTENT_STR)
print(URLS)


# RSS_CONTENT = requests.get(RSS_FEED_LIST['Pauls_Hardware'])
# print(RSS_CONTENT.status_code)
# print(RSS_CONTENT.content)


# for URL in RSS_FEED_LIST:
#     print(RSS_FEED_LIST[URL])