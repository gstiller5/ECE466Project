from pandas import *

def read_tweets_elon():
    file = open('elonmusk_tweets.csv', 'rb')
    file_list = read_csv(file)
    tweets = []
    for line in file_list["text"]:
        line = line[2:-1]
        tweets.append([line])
        # print(line)
    return tweets

def read_tweets_donald():
    file = open('trump_tweets.csv', 'rb')
    file_list = read_csv(file)
    tweets = []
    for line in file_list["text"]:
        tweets.append([line])
    return tweets
