import nltk
from nltk.corpus import stopwords
import spacy
nlp = spacy.load("en_core_web_sm")
pos=0
neg=0
neu=0
def my_function_pos(dec, dec1):#positive
    with open("text") as openfile:
        for line in openfile:
            for part in line.split():
                if dec in part:
                    print('Aspect:',dec1,'  ' 'description:',dec, '', 'Sentiment score: 1.0')
                    return 1
                    break
def my_function_neg(dec, dec1):#negative
    with open("text") as openfile:
        for line in openfile:
            for part in line.split():
                if dec== part:
                    print('Aspect:',dec1,'  ' 'description:',dec, '', 'Sentiment score:- 1.0')
                    return -1
                    break
with open("path") as f:
    for line in f:
        txt = line.lower()
        sentList = nltk.sent_tokenize(txt)
        for line in sentList:
            txt_list = nltk.word_tokenize(line)
            taggedList = nltk.pos_tag(txt_list)
        newwordList = []
        flag = 0
        for i in range(0, len(taggedList) - 1):
            if (taggedList[i][1] == "NN" and taggedList[i + 1][1] == "NN"):
                newwordList.append(taggedList[i][0] + taggedList[i + 1][0])
                flag = 1
            else:
                if (flag == 1):
                    flag = 0
                    continue
                newwordList.append(taggedList[i][0])
                if (i == len(taggedList) - 2):
                    newwordList.append(taggedList[i + 1][0])
        finaltxt = ' '.join(word for word in newwordList)
        stop_words = set(stopwords.words('english'))
        new_txt_list = nltk.word_tokenize(finaltxt)
        wordsList = [w for w in new_txt_list]
        taggedList = nltk.pos_tag(wordsList)
        featureList = []
        categories = []
        fcluster = []
        totalfeatureList = []
        finalcluster = []
        dic = {}
        for i in taggedList:
            if (i[1] == 'JJ' or i[1] == 'NN' or i[1] == 'JJR' or i[1] == 'NNS' or i[1] == 'RB'):
                featureList.append(list(i))
                totalfeatureList.append(list(i))
                categories.append(i[0])
        aspects = []
        prepend1 = ''
        doc = nlp(finaltxt)
        aspects = []
        descriptive_term = ''
        target = ''
        for token in doc:
            if (token.dep_ == 'nsubj') and token.pos_ == 'NOUN':
                target = token.text
            if token.dep_ == 'neg':
                prepend1 = 'Not'
            if token.pos_ == 'ADJ':
                prepend = ''
                for child in token.children:
                    if child.pos_ != 'ADV':
                        continue
                    prepend += child.text + ' '
                descriptive_term = prepend1 + ' ' + prepend + token.text
                prepend1 = ''
                aspects.append({'aspect': target, 'description': descriptive_term})
        teachaspc = []
        from textblob import TextBlob
        for aspect in aspects:
            dec= aspect['description']
            teachaspc.append(dec)
            dec1=aspect['aspect']
            teachaspc.append(dec)
            dec=dec.lstrip()
            aspect= TextBlob(dec).sentiment
            if aspect[0]==0:
                if (my_function_pos(dec, dec1)!=1 and my_function_neg(dec, dec1)!=1):
                        print('Aspect:', dec1, '  ' 'description:', dec, '', 'Sentiment score:0')
                        neu = neu + 1
            if aspect[0] == 0:
                if my_function_pos(dec, dec1)==1:
                    pos = pos + 1
                if my_function_neg(dec, dec1)==-1:
                    neu = neu + 1

            if aspect[0] != 0:
                print('Aspect:', dec1, '  ' 'description:', dec, '', 'Sentiment score:', aspect[0])
                if aspect[0] > 0:
                    pos = pos + 1
                else:
                    neg = neg + 1
print(pos,neg,neu)
import barchart
import cloud
barchart.shape(pos,neg,neu)
cloud



