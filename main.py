import matplotlib.pyplot as plt
from read_tweets import *

file = open("lexicon_easy.csv", "rb")
words = []
words_no_sent = []
pos = 0
neg = 0
neu = 0
provocative = 0

for f in file:
    new_word = str(f).split(',')
    new_word[0] = new_word[0][2:] # clearing out extra characters
    words_no_sent.append(new_word[0])
    new_word[1] = new_word[1][:-3]
    words.append(new_word)

tweets = []
# tweets = read_tweets_elon()
tweets = read_tweets_donald()
# example tweets
tweets.append(["Griffin is the best thing to happen to python coding ever"])
tweets.append(["The party pigs are raw at soccer and will never be forgotten"])
tweets.append(["I hate ASU"])
tweets.append(["ASU is the worst school in the state of Arizona"])
tweets.append(["Sean miller is the best coach in college basketball"])
tweets.append(["I am glad that Rich Rodriguez was fired, he was not helping the program"])
tweets.append(["Griffin is the man - abundant abundance absolve positive good great bad poor"])
tweets.append(["this one has no_provocative_words"])

for x in tweets:
    x.append(0)
    x.append(0)
    for y in x[0].split(' '):
        if y in words_no_sent:
            x[2] += 1 # add the number of words that are possible to analyze
            x[1] += int(words[words_no_sent.index(y)][1]) # add the sentiment of the word to the tweet's score
    if x[2] != 0:
        provocative += 1

# sort the tweets by score and print the list
tweets.sort(key=lambda x: x[1])
tweets.reverse()
for x in tweets:
    print('Words: ' + str(x[2]) + '\tScore: ' + str(x[1]) + '\tTweet: ' + x[0])
    if x[1] > 0:
        pos += 1
    elif x[1] == 0:
        neu +=1
    else:
        neg += 1

plt.bar(range(3), [pos, neu, neg])
plt.xticks(range(3), ["Positive", "Neutral", "Negative"])
plt.title("Tweet Sentiment Analysis")
plt.ylabel("# of Tweets")

print()
print('Number of tweets: ' + str(len(tweets)))
print('Number of tweets with provocative words: ' + str(provocative))
print('Percentage of tweets with provocative language: ' + str((provocative/len(tweets))*100))

plt.show()