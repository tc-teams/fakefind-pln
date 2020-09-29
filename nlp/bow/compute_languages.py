# -*- coding: utf-8 -*-
import re
import unicodedata
from math import sqrt

import nltk
from nltk.tokenize import sent_tokenize, word_tokenize, RegexpTokenizer
from nltk.probability import FreqDist
from nltk.stem.rslp import RSLPStemmer
from nltk.corpus import stopwords


def _clean_text(document):
    nfkd = unicodedata.normalize('NFKD', document)
    text = u"".join([c for c in nfkd if not unicodedata.combining(c)])

    return re.sub('[^a-zA-Z0-9 \\\]', '',text)

def _remove_stop_words(document):
    text_tokens = word_tokenize(document)

    tokens_without_sw = [word for word in text_tokens if not word in stopwords.words()]
    filtered_sentence = (" ").join(tokens_without_sw)
    return filtered_sentence


def _cts_tokenize(document):

    tokenizer = RegexpTokenizer(r'\W|\s+',' ')
    sentence = []

    for i in sent_tokenize(document):
        sentence.append(i.lower())

    tokens = _cts_stopwords([tokenizer.tokenize(i) for i in sentence])
    return tokens


def _cts_stopwords(tokens):

    stop_words = set(stopwords.words('portuguese'))
    without_stop_words = []
    for i in tokens:
       without_stop_words.extend([word for word in i if not word in stop_words])
    
    return without_stop_words


def _square_rooted(x):

    return round(sqrt(sum([a*a for a in x])),3)


def _cosine_similarity(x, y):

    input1 = {}
    input2 = {}
    vector1 = []
    vector2 = []

    if len(x) > len(y):
        input1 = x
        input2 = y
    else:
        input1 = y
        input2 = x


    vector1 = list(input1.values())

    for k in input1.keys():
        if k in input2:
            vector2.append(float(input2[k]))
        else :
            vector2.append(float(0))


    numerator = sum(a*b for a,b in zip(vector2,vector1))
    denominator = _square_rooted(vector1)*_square_rooted(vector2)
    return round(numerator/float(denominator),3)


def _create_frequency_table(text_string) -> dict:

    words = _cts_tokenize(text_string)
    rslps = RSLPStemmer()

    freqTable = dict()
    for word in words:
        word = rslps.stem(word)
        if word in freqTable:
            freqTable[word] += 1
        else:
            freqTable[word] = 1
    
    return freqTable


def _create_summarization(text):

    freq_table = _create_frequency_table(text)

    sentences = sent_tokenize(text)

    sentence_scores = _score_sentences(sentences, freq_table)

    threshold = _find_average_score(sentence_scores)

    summary = _generate_summary(sentences, sentence_scores, 1 * threshold)

    return summary

def _score_sentences(sentences, freqTable) -> dict:

    sentenceValue = dict()

    for sentence in sentences:

        word_count_in_sentence_except_stop_words = 0
        for wordValue in freqTable:
            if wordValue in sentence.lower():
                word_count_in_sentence_except_stop_words += 1
                if sentence[:10] in sentenceValue:
                    sentenceValue[sentence[:10]] += freqTable[wordValue]
                else:
                    sentenceValue[sentence[:10]] = freqTable[wordValue]

        if sentence[:10] in sentenceValue:
            sentenceValue[sentence[:10]] = sentenceValue[sentence[:10]] / word_count_in_sentence_except_stop_words

    return sentenceValue


def _find_average_score(sentenceValue) -> int:

    sumValues = 0
    for entry in sentenceValue:
        sumValues += sentenceValue[entry]

    average = (sumValues / len(sentenceValue))

    return average


def _generate_summary(sentences, sentenceValue, threshold):
    sentence_count = 0
    summary = ''

    for sentence in sentences:
        if sentence[:10] in sentenceValue and sentenceValue[sentence[:10]] >= (threshold):
            summary += " " + sentence
            sentence_count += 1

    return summary

def bow(description, document):

    desc_freq = _create_frequency_table(description)

    similarity = _cosine_similarity(desc_freq, doc_freq)

    percentage = similarity*100

    return percentage

def summary(document):
    doc =  _create_summarization(document)
    doc_cleaned = _clean_text(doc)
    text = _remove_stop_words(doc_cleaned)
    rslps = RSLPStemmer()
    return  rslps.stem(text)
