
import nltk 
import re
import numpy as np 
import heapq 
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.probability import FreqDist
from nltk.corpus import stopwords
from nltk import ngrams

#TODO implementar função para ser chamada pela nossa API para Tokenization
text = "Hello word"
text2 = open("teste.txt", "r")
text3 = open("teste2.txt", "r")

def text_cleaner(text):
    '''
        Convert text to lower case, remove all non-word characters 
        and remove all punctuations.
    '''
    dataset = nltk.sent_tokenize(text.read()) 
    for i in range(len(dataset)):
        dataset[i] = dataset[i].lower()
        dataset[i] = re.sub(r'\W', ' ', dataset[i])
        dataset[i] = re.sub(r'\s+', ' ', dataset[i])
    return dataset


def word_extraction(dataset):
    '''
        Declare a dictionary to hold the bag of words, tokenize each sentence 
        to words, and for each word in sentence, check if the word exists in the 
        dictionary. If it does, then increment its count by 1. If it doesn’t, add 
        it to the dictionary and set its count as 1.
    '''
    ignore = set(stopwords.words('portuguese'))
    word2count = {}
    for data in dataset:
        words = nltk.word_tokenize(data)
        for word in words:
            if word not in ignore:
                if word not in word2count.keys():
                    word2count[word] = 1
                else:
                    word2count[word] += 1

    freq_words = heapq.nlargest(100, word2count, key=word2count.get)
    return freq_words

'''
In this step we construct a vector, which would tell us whether a word in each 
sentence is a frequent word or not. If a word in a sentence is a frequent word, 
we set it as 1, else we set it as 0.
'''
# X = [] 
# for data in dataset: 
#     vector = [] 
#     for word in freq_words: 
#         if word in nltk.word_tokenize(data): 
#             vector.append(1) 
#         else: 
#             vector.append(0) 
#     X.append(vector) 
# X = np.asarray(X)

# print(X)

'''
that finds the most common ngrams that contain a particular target word.
'''

# fd = FreqDist(ng
#               for ng in ngrams(text2, 5)
#               if freq_words in ng)
# for hit in fd.setdefault():
#     print(' '.join(hit))

def strike_match(vec1, vec2):
    '''
        Find the percentage of matching words
    '''
    pairs1 = vec1
    pairs2 = vec2
    union  = len(pairs1) + len(pairs2)
    hit_count = 0
    for x in pairs1:
        for y in pairs2:
            if x == y:
                hit_count += 1
                break
    return (2.0 * hit_count) / union

print("Porcentagem", strike_match(word_extraction(text_cleaner(text2)), 
                                   word_extraction(text_cleaner(text3))))

tokenized_text = sent_tokenize(text)
print("sent_tokenize", tokenized_text)

tokenized_word = word_tokenize(text)
print("word_tokenize", tokenized_word)

#TODO implementar função para ser chamada pela nossa API para Frequency Distribution
fdist = FreqDist(tokenized_word)
print("frequencia", fdist)

# fdist = FreqDist(word.lower() for word in word_tokenize(sent))
#TODO analisar outros métodos
