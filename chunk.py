import nltk
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
words=nltk.word_tokenize('text')
print(words)
tagged=nltk.pos_tag(words)
print(tagged)
new_gram_np=r"NP:{<DT>? <NN>*<NN>|<NN>*<NNS>}"
parser=nltk.RegexpParser(new_gram_np)
chunked=parser.parse(tagged)
print(chunked)
chunked.draw()
import nltk
lines = 'text'
is_noun = lambda pos: pos[:2] == 'NN'
tokenized = nltk.word_tokenize(lines)
nouns = [word for (word, pos) in nltk.pos_tag(tokenized) if is_noun(pos)]
print(nouns)
