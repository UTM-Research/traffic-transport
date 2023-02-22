import stanfordnlp
stanfordnlp.download('en')
from nltk.parse.stanford import StanfordParser
parser=StanfordParser(model_path=" ")
list(parser.raw_parse("txt"))

