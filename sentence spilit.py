import nltk
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk import tokenize
words=nltk.word_tokenize('text',)
print(words)
txt='text'
a_list = nltk.tokenize.sent_tokenize(txt, ","".")
print(a_list[0])