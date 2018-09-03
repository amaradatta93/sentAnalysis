import datetime
import os
import time
from urllib.parse import urlencode

import requests
from requests_oauthlib import OAuth1

CONSUMER_KEY = os.environ.get('CONSUMER_KEY')
CONSUMER_SECRET = os.environ.get('CONSUMER_SECRET')
ACCESS_TOKEN = os.environ.get('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.environ.get('ACCESS_TOKEN_SECRET')
hashtags = ['#SpaceX', '#Tesla', '#Paypal']


def url_response(url, entities):
    params = urlencode(entities)
    url_final = url + params
    auth = OAuth1(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    return_response = requests.get(url_final, auth=auth)
    return return_response.json()


def statuses_response():
    entities = dict(screen_name='elonmusk', tweet_mode='extended')
    status_response = url_response('https://api.twitter.com/1.1/statuses/user_timeline.json?', entities)
    return status_response


def hashtags_response(index):
    entities = dict(q=hashtags[index], count=10, result_type='recent', tweet_mode='extended')
    hashtag_response = url_response('https://api.twitter.com/1.1/search/tweets.json?', entities)
    return hashtag_response


def convert_to_timestamp(twitter_date):
    ts = datetime.datetime.fromtimestamp(time.mktime(time.strptime(twitter_date, '%a %b %d %H:%M:%S +0000 %Y')))
    stamp = datetime.datetime.timestamp(ts)
    return stamp
