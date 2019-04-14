


import unidecode
import string



def remove_punct(x):
    return x.translate(str.maketrans('', '', string.punctuation))


def remove_multiple_spaces(x):
    return " ".join(x.split())


def remove_unicode(x):
    return unidecode.unidecode(x)


def remove_stop_words(x):
    pass