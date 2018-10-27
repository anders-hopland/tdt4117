import random; random.seed(123)
import string
import codecs
from nltk.stem.porter import PorterStemmer
import re

stemmer = PorterStemmer()
translator = str.maketrans('', '', string.punctuation+"\n\r\t")

f = codecs.open("pg3300.txt", "r", "utf-8")

text = f.read()
paragraphs = text.split('\r\n\r\n') # Split into seperate paragraphs
paragraphs = [p for p in paragraphs if 'Gutenberg' not in p] # Filter out headers and footers
words = [re.findall(r'\S+', w) for w in paragraphs]
words = [str(w).translate(translator).lower() for p in words for w in p]
processed_words = []
for p in words:
    for w in words:
        
#stemmed_words = [stemmer.stem(w) for w in words]
'''
for p in words:
    print(p)
    for w in p:
        print(w)
        print('\n')
'''


#print(len(paragraphs))
#print(paragraphs[100])
#print(words[100][11])
print(str(words[10]))
'''for p in words:
    for w in p:
        print(w)

'''