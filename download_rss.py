# import all the shit
import requests
import feedparser
from RSS_Sources import RSS_FEED_LIST

# do the things
print(RSS_FEED_LIST['Pauls_Hardware'])
print('\r\n')

print(feedparser.parse(RSS_FEED_LIST['Pauls_Hardware']))


# RSS_CONTENT = requests.get(RSS_FEED_LIST['Pauls_Hardware'])
# print(RSS_CONTENT.status_code)
# print(RSS_CONTENT.content)


# for URL in RSS_FEED_LIST:
#     print(RSS_FEED_LIST[URL])