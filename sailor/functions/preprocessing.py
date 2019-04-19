


import unidecode
import string

# NLTK
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.collocations import BigramCollocationFinder




def remove_punct(x):
    """Remove punctation from a string

    Args:
        x (str): input string to transform

    Returns
        str - the transformed string
    """
    return x.translate(str.maketrans('', '', string.punctuation))


def remove_multiple_spaces(x):
    """Remove multiple spaces from a string

    Args:
        x (str): input string to transform

    Returns
        str - the transformed string
    """
    return " ".join(x.split())


def remove_unicode(x):
    """Remove unicode characters from a string
    For example the accents in French

    Args:
        x (str): input string to transform

    Returns
        str - the transformed string
    """
    return unidecode.unidecode(x)



def clean_tokens(x,stopwords = None,vocab = None,min_len = 1,max_len = 30):
    vocab = vocab if vocab is not None else []
    if stopwords is not None:
        vocab_stopwords = get_stop_words(stopwords)
        vocab.extend(vocab_stopwords)
    tokens = []
    for token in x:
        if token in vocab: continue
        if len(token) <= min_len: continue
        if len(token) >= max_len: continue
        tokens.append(token)
    return tokens






def tokenize(x,lang = "english"):
    """TODO 
        - switch to wordpunct_tokenize
        - Language mapping
    """

    return word_tokenize(x,lang)



def get_stop_words(lang = None):
    if lang is None:
        lang = list(stopwords.fileids())
    if not isinstance(lang,list):
        return list(set(stopwords.words(lang)))
    else:
        return [x for l in lang for x in get_stop_words(l)]





def find_bigrams(documents,freq_filter = 5,n = 100):
    measure = nltk.collocations.BigramAssocMeasures()
    finder = BigramCollocationFinder.from_documents(documents)
    finder.apply_freq_filter(freq_filter)
    bigrams = finder.nbest(measure.pmi,n)
    return bigrams


def replace_bigrams(x,bigrams):
    for a,b in bigrams:
        old_bigram = f"{a} {b}"
        new_bigram = f"{a}_{b}"
        x = x.replace(old_bigram,new_bigram)
    return x


