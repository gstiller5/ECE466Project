import tweepy
from tweepy import OAuthHandler
# from tweepy import Stream
# from tweepy.streaming import StreamListener

consumer_key = 'hok2wO0GrKJ7szEQ5rwx9ycU4'
consumer_secret = '1BdV005A5qbEIflaOFtxmapdA9bxEEzZO6m6D97rIfxcgzrwUO'
access_token = '280777286-P2NQbEjOYm9SVDneEuyfoVkifSaklyCYyoipugze'
access_secret = 'trg5XWVHIq5rJbD1WIDVIaZBltw6s8SLxGhnpdAWV2tp5'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

def read_tweets_elon():
    muskTweets = api.user_timeline(screen_name='realDonaldTrump', count=200, include_rts=False)
    tweets = []
    for x in muskTweets:
        tweets.append(x.text.split("`"))
    return tweets

def read_tweets_donald():
    trumpTweets = api.user_timeline(screen_name='realDonaldTrump', count=200, include_rts=False)
    tweets = []
    for x in trumpTweets:
        tweets.append(x.text.split("`"))
    return tweets