import os
import pprint
from urllib.parse import urlencode

import requests
from requests_oauthlib import OAuth1

CONSUMER_KEY = os.environ.get('CONSUMER_KEY')
CONSUMER_SECRET = os.environ.get('CONSUMER_SECRET')
ACCESS_TOKEN = os.environ.get('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.environ.get('ACCESS_TOKEN_SECRET')

tweets = []

params_status = urlencode(dict(screen_name='elonmusk', tweet_mode='extended'))
params_hashtag = urlencode(dict(q='#SpaceX', count=10, result_type='recent', tweet_mode='extended'))

url_status = 'https://api.twitter.com/1.1/statuses/user_timeline.json?{0}'.format(params_status)
url_hashtag = 'https://api.twitter.com/1.1/search/tweets.json?{0}'.format(params_hashtag)

auth = OAuth1(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

return_response_status = requests.get(url_status, auth=auth)
return_response_hashtag = requests.get(url_hashtag, auth=auth)

json_response_status = return_response_status.json()
json_response_hashtag = return_response_hashtag.json()

for s in json_response_status:
    tweets.append(s['full_text'])

for h in json_response_hashtag['statuses']:

    if 'retweeted_status' in h.keys():
        tweets.append(h['retweeted_status']['full_text'])
    else:
        tweets.append(h['full_text'])

pprint.pprint(set(tweets))

# connection = psycopg2.connect("dbname=tweets user=sentanalysis")


##number of tweets at one hit ,

# push pyscopg2 database :
# data base table tweets , id extract
# rate limit
#  number of tweets
#
#
# ============================================
# sleep


# import inspect
# print(inspect.signature(twitter.Api.__init__))
