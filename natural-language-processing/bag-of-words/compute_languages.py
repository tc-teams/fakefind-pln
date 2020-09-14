import nltk
nltk.download('stopwords')
nltk.download('punkt')

import heapq 
from nltk.tokenize import RegexpTokenizer
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords


def cts_tokenize(document):
 
    tokenizer = RegexpTokenizer(r'\W|\s+',' ')
    sentence = []
    
    for i in nltk.sent_tokenize(document):
        sentence.append(i.lower())

    tokens = cts_stopwords([tokenizer.tokenize(i) for i in sentence])
    return tokens

def cts_stopwords(tokens):

    stop_words = set(stopwords.words('portuguese'))
    without_stop_words = []
    for i in tokens:
       without_stop_words.extend([word for word in i if not word in stop_words])
    
    return without_stop_words

def cts_match(vec1, vec2):
    
    pairs1 = vec1
    pairs2 = vec2
    union  = len(pairs1) + len(pairs2)
    hit_count = 0
    for x in pairs1:
        #print("valor de x:",x)
        for y in pairs2:
            if x == y:
                #print("valor de y:",y)
                hit_count += 1
                break
    return str(((2.0 * hit_count) / union))


def bow(document):
    bag = cts_tokenize(document)
    frequence = {}
    for word in bag:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
           if word not in frequence.keys():
                frequence[word] = 1
           else:
                frequence[word] += 1
    return frequence
