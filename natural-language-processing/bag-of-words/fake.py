import nltk
from nltk.tokenize import sent_tokenize

#TODO implementar função para ser chamada pela nossa API para Tokenization
text="""Hello word"""

tokenized_text=sent_tokenize(text)
print(tokenized_text)

#TODO implementar função para ser chamada pela nossa API para Stopwords

from nltk.tokenize import word_tokenize

tokenized_word=word_tokenize(text)
print(tokenized_word)

#TODO implementar função para ser chamada pela nossa API para Frequency Distribution
from nltk.probability import FreqDist
fdist = FreqDist(tokenized_word)
print(fdist)

#TODO analisar outros métodos
