from textblob import TextBlob
import nltk
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
text = "text"
obj = TextBlob(text)
sentiment = obj.sentiment.polarity
print(sentiment)

from nltk.sentiment import SentimentIntensityAnalyzer
sia = SentimentIntensityAnalyzer()
s=sia.polarity_scores("text")
print(s)

