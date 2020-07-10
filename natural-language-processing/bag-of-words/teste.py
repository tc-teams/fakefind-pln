import nltk 
import re
import math

import pandas as pd

from collections import Counter
from unicodedata import normalize
from nltk import ngrams

#Regex para encontrar tokens
REGEX_WORD = re.compile(r'\w+')
#Numero de tokens em sequencia
N_GRAM_TOKEN = 3

#Faz a normalizacao do texto removendo espacos a mais e tirando acentos
def text_normalizer(src):
    return re.sub('\s+', ' ',
                normalize('NFKD', src)
                   .encode('ASCII','ignore')
                   .decode('ASCII')
           ).lower().strip()

#Faz o calculo de similaridade baseada no coseno
def cosine_similarity(vec1, vec2):
    intersection = set(vec1.keys()) & set(vec2.keys())
    numerator = sum([vec1[x] * vec2[x] for x in intersection])

    sum1 = sum([vec1[x]**2 for x in vec1.keys()])
    sum2 = sum([vec2[x]**2 for x in vec2.keys()])
    denominator = math.sqrt(sum1) * math.sqrt(sum2)

    if not denominator:
        return 0.0
    else:
        coef = float(numerator) / denominator
        if coef > 1:
            coef = 1
        return coef

#Monta o vetor de frequencia da sentenca
def sentence_to_vector(text, use_text_bigram):
    words = REGEX_WORD.findall(text)
    accumulator = []
    for n in range(1,N_GRAM_TOKEN):
        gramas = ngrams(words, n)
        for grama in gramas:
            accumulator.append(str(grama))

    if use_text_bigram:
        pairs = get_text_bigrams(text)
        for pair in pairs:
            accumulator.append(pair)

    return Counter(accumulator)

#Obtem a similaridade entre duas sentencas
def get_sentence_similarity(sentence1, sentence2, use_text_bigram=False):
    vector1 = sentence_to_vector(text_normalizer(sentence1), use_text_bigram)
    vector2 = sentence_to_vector(text_normalizer(sentence2), use_text_bigram)
    return cosine_similarity(vector1, vector2)

#Metodo de gerar bigramas de uma string
def get_text_bigrams(src):
    s = src.lower()
    return [s[i:i+2] for i in range(len(s) - 1)]

if __name__ == "__main__":
    text1 = open("teste.txt", "r")
    text2 = open("teste2.txt", "r")

    w1 = text1.read()
    w2 = text2.read()

    print('Busca: ' + w1)

    #Nivel de aceite (40%)
    cutoff = 0.20
    #Sentenças similares
    result = []

    
    print('\nCosine Sentence --- ' + w2)

    #Calculo usando similaridade do coseno com apenas tokens
    similarity_sentence = get_sentence_similarity(w1, w2)
    print('\tSimilarity sentence: ' + str(similarity_sentence))

    if similarity_sentence >= cutoff:
        result.append((w2, similarity_sentence))

    print('\nResultado:')
    #Exibe resultados
    for data in result:
        print(data)