import pprint

from utils import statuses_response, hashtags_response, convert_to_timestamp, hashtags

tweets = []


def status_tweets():
    response = statuses_response()
    # pprint.pprint(response)
    for status in response:
        tweets.append({
            'timestamp': convert_to_timestamp(status['created_at']),
            'hashtag': None,
            'author': status['user']['name'],
            'tweet': status['full_text'],
        })
    return tweets


def hashtag_tweets(index):
    response = hashtags_response(index)
    for hashtag in response['statuses']:
        if 'retweeted_status' in hashtag.keys():
            tweets.append({
                'timestamp': convert_to_timestamp(hashtag['created_at']),
                'hashtag': hashtags[index],
                'author': hashtag['retweeted_status']['user']['name'],
                'tweet': hashtag['retweeted_status']['full_text'],
            })
        else:
            tweets.append({
                'timestamp': convert_to_timestamp(hashtag['created_at']),
                'hashtag': hashtags[index],
                'author': hashtag['user']['name'],
                'tweet': hashtag['full_text'],
            })


# status_tweets()
hashtag_tweets(0)
pprint.pprint(tweets)

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
