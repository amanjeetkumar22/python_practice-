#sentiment analysis
import numpy as np # linear algebra
import pandas as pd # data processing , csv files I/O(eg.pd.read_csv)
import string #special operation on string 
import spacy # language models 

from matplotlib.pyplot import imread 
from matplotlib import pyplot as plt 
from wordcloud import WordCloud
# matplotlib inline 

import pandas 
b=pd.read_csv("https://gist.github.com/jamestut/d5bbaea1ba0503a6f7270f75e6777a77")
book =[x.strip() for x in b.x]
book =[x for x in book if x]