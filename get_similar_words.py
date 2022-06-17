from inltk.inltk import get_similar_sentences
from setup import language
import pandas as pd

def get_similar(sentence, n):
    return get_similar_sentences(sentence, n,  language, degree_of_aug=0.9)


temp = pd.DataFrame()
temp['similar_words'] = get_similar('ਸਤ ਸ੍ਰੀ ਅਕਾਲ',10)
temp.to_csv('temp.csv')

