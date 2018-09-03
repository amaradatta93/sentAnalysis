import os
from urllib.parse import urlencode

import requests
from requests_oauthlib import OAuth1

CONSUMER_KEY = os.environ.get('CONSUMER_KEY')
CONSUMER_SECRET = os.environ.get('CONSUMER_SECRET')
ACCESS_TOKEN = os.environ.get('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.environ.get('ACCESS_TOKEN_SECRET')


def url_response(url, **kwargs):
    params = urlencode(kwargs)
    url_final = url + params
    print(url_final)
    auth = OAuth1(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    return_response = requests.get(url_final, auth=auth)
    return return_response.json()


def statuses_response():
    status_response = url_response('https://api.twitter.com/1.1/statuses/user_timeline.json?', screen_name='elonmusk',
                                   tweet_mode='extended')
    return status_response


def hashtags_response(index):
    hashtags = ['#SpaceX', '#Tesla', '#Paypal']
    hashtag_response = url_response('https://api.twitter.com/1.1/search/tweets.json?', q=hashtags[index], count=10,
                                    result_type='recent', tweet_mode='extended')
    return hashtag_response
