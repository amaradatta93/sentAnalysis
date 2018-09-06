import psycopg2

from utils import DB_NAME, DB_USER, DB_PASSWORD


def save_tweets_to_db():
    # db_credentials = "dbname=DB_NAME user=DB_USER password=DB_PASSWORD")
    # connection = psycopg2.connect("dbname=tweets user=sentanalysis password=password")
    connection = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD)
    curr = connection.cursor()
    iq = "INSERT into tweet_collection VALUES {}".format("(2, 'w', 'e', 'd')")
    curr.execute(iq)
    connection.commit()
    curr.close()
    connection.close()


save_tweets_to_db()

##number of tweets at one hit ,

# push pyscopg2 database :
# data base table tweets , id extract
# rate limit
#  number of tweets
#
#
# ============================================
# sleep


