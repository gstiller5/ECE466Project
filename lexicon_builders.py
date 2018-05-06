from pandas import *


def build_1850_lexicon():
    file = open('1850.tsv', 'rb')
    words = []
    scores = []
    for f in file:
        word = str(f).split('\\t')[0][2:]
        words.append(word)
        score = str(f).split('\\t')[1]
        scores.append(score)
        # print(word + '    \t ' + score)
    return words, scores


def build_1900_lexicon():
    file = open('1900.tsv', 'rb')
    words = []
    scores = []
    for f in file:
        word = str(f).split('\\t')[0][2:]
        words.append(word)
        score = str(f).split('\\t')[1]
        scores.append(score)
        # print(word + '    \t ' + score)
    return words, scores


def build_1950_lexicon():
    file = open('1950.tsv', 'rb')
    words = []
    scores = []
    for f in file:
        word = str(f).split('\\t')[0][2:]
        words.append(word)
        score = str(f).split('\\t')[1]
        scores.append(score)
        # print(word + '    \t ' + score)
    return words, scores


def build_2000_lexicon():
    file = open('2000.tsv', 'rb')
    words = []
    scores = []
    for f in file:
        word = str(f).split('\\t')[0][2:]
        words.append(word)
        score = str(f).split('\\t')[1]
        scores.append(score)
        # print(word + '    \t ' + score)
    return words, scores


def build_standard_lexicon():
    words = []
    scores = []
    file = open('lexicon_easy.csv', 'rb')

    for f in file:
        new_word = str(f).split(',')
        new_word[0] = new_word[0][2:]  # clearing out extra characters
        words.append(new_word[0])
        new_word[1] = new_word[1][:-3]
        scores.append(new_word[1])
    return words, scores


def build_women_lexicon():
    file = open('AskWomen.tsv', 'rb')
    words = []
    scores = []
    for f in file:
        word = str(f).split('\\t')[0][2:]
        words.append(word)
        score = str(f).split('\\t')[1]
        scores.append(score)
        # print(word + '    \t ' + score)
    return words, scores


def build_men_lexicon():
    file = open('AskMen.tsv', 'rb')
    words = []
    scores = []
    for f in file:
        word = str(f).split('\\t')[0][2:]
        words.append(word)
        score = str(f).split('\\t')[1]
        scores.append(score)
        # print(word + '    \t ' + score)
    return words, scores
