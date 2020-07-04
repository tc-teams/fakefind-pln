
import nltk 
import re
import numpy as np 
import heapq 
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.probability import FreqDist

#TODO implementar função para ser chamada pela nossa API para Tokenization
text = "Hello word"
text2 = open("teste.txt", "r")

'''
First, we will convert text to lower case, then remove all non-word characters 
and remove all punctuations.
'''
dataset = nltk.sent_tokenize(text2.read()) 
for i in range(len(dataset)):
    dataset[i] = dataset[i].lower()
    dataset[i] = re.sub(r'\W', ' ', dataset[i])
    dataset[i] = re.sub(r'\s+', ' ', dataset[i])

# for i in range(len(dataset)): 
#     print(dataset[i])

'''
Next, we declare a dictionary to hold our bag of words, tokenize each sentence 
to words, and for each word in sentence, we check if the word exists in our 
dictionary. If it does, then we increment its count by 1. If it doesn’t, we add 
it to our dictionary and set its count as 1.
'''
word2count = {}
for data in dataset:
    words = nltk.word_tokenize(data)
    for word in words:
        if word not in word2count.keys():
            word2count[word] = 1
        else:
            word2count[word] += 1

freq_words = heapq.nlargest(100, word2count, key=word2count.get)

# print("Palavras frequentes", freq_words)

'''
In this step we construct a vector, which would tell us whether a word in each 
sentence is a frequent word or not. If a word in a sentence is a frequent word, 
we set it as 1, else we set it as 0.
'''
X = [] 
for data in dataset: 
    vector = [] 
    for word in freq_words: 
        if word in nltk.word_tokenize(data): 
            vector.append(1) 
        else: 
            vector.append(0) 
    X.append(vector) 
X = np.asarray(X)

print(X)

tokenized_text = sent_tokenize(text)
print("sent_tokenize", tokenized_text)

tokenized_word = word_tokenize(text)
print("word_tokenize", tokenized_word)

#TODO implementar função para ser chamada pela nossa API para Frequency Distribution
fdist = FreqDist(tokenized_word)
print("frequencia", fdist)

# fdist = FreqDist(word.lower() for word in word_tokenize(sent))
#TODO analisar outros métodos
