# import all the shit
import requests
from RSS_Sources import RSS_FEED_LIST

# do the things
print(RSS_FEED_LIST['Pauls_Hardware'])
print('\r\n')

for URL in RSS_FEED_LIST:
    print(RSS_FEED_LIST[URL])