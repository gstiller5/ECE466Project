import matplotlib.pyplot as plt
from read_tweets import *
from lexicon_builders import *
import re
import numpy

pos = 0
neg = 0
neu = 0
lex_words = 0

#set up the lexicon
words = []
scores = []
# words, scores = build_standard_lexicon()
words, scores = build_1850_lexicon()
# words, scores = build_1900_lexicon()
# words, scores = build_1950_lexicon()
# words, scores = build_2000_lexicon()

pos1 = 0
neg1 = 0
neu1 = 0
lex_words1 = 0

words1 = []
scores1 = []
# words1, scores1 = build_standard_lexicon()
# words1, scores1 = build_1850_lexicon()
# words1, scores1 = build_1900_lexicon()
# words1, scores1 = build_1950_lexicon()
words1, scores1 = build_2000_lexicon()

#set up the tweet list
tweets = []
# tweets = read_tweets_elon()
tweets = read_tweets_donald()

tweets1 = []
# tweets1 = read_tweets_elon()
tweets1 = read_tweets_donald()

# example tweets
# tweets.append(["Griffin is the best thing to happen to python coding ever"])
# tweets.append(["The party pigs are raw at soccer and will never be forgotten"])
# tweets.append(["I hate ASU"])
# tweets.append(["ASU is the worst school in the state of Arizona"])
# tweets.append(["Sean miller is the best coach in college basketball"])
# tweets.append(["I am glad that Rich Rodriguez was fired, he was not helping the program"])
# tweets.append(["Griffin is the man - abundant abundance absolve positive good great bad poor"])
# tweets.append(["this one has no_provocative_words"])

for x in tweets: #cycle through tweet list
    x.append(0.0)
    x.append(0)
    for y in x[0].split(' '): # seperate the tweet by the word
        # y = y.strip(['.', ',', '!', '?']) # strip off punctuation
        y = re.sub('[(){}<>!?.,#]', '', y)
        if y in words: # check if the word is in the lexicon
            x[2] += 1 # add the number of words that are possible to analyze
            x[1] += float(scores[words.index(y)]) # add the sentiment of the word to the tweet's score
    if x[2] != 0:
        lex_words += 1

# sort the tweets by score and print the list
tweets.sort(key=lambda x: x[1])
tweets.reverse()
for x in tweets:
    print('Words: ' + str(x[2]) + '\tScore: ' + '%.2f'%x[1] + '\tTweet: ' + x[0])
    if x[1] > 0:
        pos += 1
    elif x[1] == 0:
        neu +=1
    else:
        neg += 1

# for the second set
for x in tweets1: #cycle through tweet list
    x.append(0.0)
    x.append(0)
    for y in x[0].split(' '): # seperate the tweet by the word
        # y = y.strip(['.', ',', '!', '?']) # strip off punctuation
        y = re.sub('[(){}<>!?.,#]', '', y)
        if y in words1: # check if the word is in the lexicon
            x[2] += 1 # add the number of words that are possible to analyze
            x[1] += float(scores1[words1.index(y)]) # add the sentiment of the word to the tweet's score
    if x[2] != 0:
        lex_words1 += 1

# sort the tweets by score and print the list
tweets1.sort(key=lambda x: x[1])
tweets1.reverse()
for x in tweets1:
    print('Words: ' + str(x[2]) + '\tScore: ' + '%.2f'%x[1] + '\tTweet: ' + x[0])
    if x[1] > 0:
        pos1 += 1
    elif x[1] == 0:
        neu1 +=1
    else:
        neg1 += 1


print()
print('Number of tweets: ' + str(len(tweets)))
print('Number of tweets with lexicon words: ' + str(lex_words))
print('Percentage of tweets with provocative language: ' + '%.2f' % ((lex_words / len(tweets)) * 100) + '%')
print()
print('Number of tweets with lexicon words: ' + str(lex_words1))
print('Percentage of tweets with provocative language: ' + '%.2f' % ((lex_words1 / len(tweets)) * 100) + '%')

# plot some findings
fig = plt.figure()
ax = fig.add_subplot(111)
plt.bar(numpy.arange(3)*2, [neg, neu, pos])
plt.bar(numpy.arange(3)*2+.8, [neg1, neu1, pos1])
ax.set_xticks(numpy.arange(3)*2+.4)
ax.set_xticklabels(["Negative", "Neutral", "Positive"])
# plt.xticks(range(3), ["Positive", "Neutral", "Negative"])
plt.title("Tweet Sentiment Analysis (1850 vs 2000 lexicon)")
plt.legend(['1850', '2000'])
plt.ylabel("# of Tweets")
plt.xlabel('Sentiment')
plt.show()