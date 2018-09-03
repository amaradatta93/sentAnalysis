import pprint

from utils import statuses_response, hashtags_response

tweets = []


def status_tweets():
    response = statuses_response()
    for status in response:
        tweets.append(status['full_text'])


def hashtag_tweets(index):
    response = hashtags_response(index)
    for hashtag in response['statuses']:
        if 'retweeted_status' in hashtag.keys():
            tweets.append(hashtag['retweeted_status']['full_text'])
        else:
            tweets.append(hashtag['full_text'])


status_tweets()
hashtag_tweets(1)
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
