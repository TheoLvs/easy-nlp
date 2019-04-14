
import pandas as pd
import numpy as np
from .exceptions import *

# Custom functions
from .functions.language import detect_language
from .functions.preprocessing import *


class Corpus(object):
    def __init__(self):
        pass

    def __len__(self):
        if hasattr(self,"data"):
            return len(self.data)
        else:
            return 0

    def _repr_html_(self):
        if hasattr(self,"data"):
            return self.data.head(10)._repr_html_()


    def load_data(self,data,column):

        if isinstance(data,pd.DataFrame):
            return data.copy(),column

        elif isinstance(data,list):
            column = "text"
            data = pd.DataFrame({column:data})
            return data,column

        else:
            raise NotImplementedError("You must load data from dataframe or a list of text")


    def load_from_pickle(self):
        pass


    def to_pickle(self):
        pass


    def detect_language(self,col = None):
        """Detect the language of the column
        TODO could be interesting with a decorator
        """

        if hasattr(self,"_col"): col = self._col
        self.data["lang"] = self.data[col].map(detect_language)




class SingleColumnCorpus(Corpus):
    def __init__(self,data,column = None,only_text = False):
        """Initialization
        """

        # Load data from inputs
        self.data,self._col = self.load_data(data,column)

        # Keep only text columns
        if only_text:
            self.data = self.data[[self.col]]

        # Create a copy of text columns for further reset
        self.data.insert(0,"raw_text",self.text.copy())

        # Tokenize
        self.tokenize()


    def __getitem__(self,key):
        if isinstance(key,int):
            return self.text.iloc[key]
        elif isinstance(key,str):
            return self.data.loc[:,key]
        else:
            raise KeyError(f"Integer keys should return rows, Str keys should return columns")


    def reset_text(self):
        """Reset text column from original text
        """
        self.text = self.data["raw_text"]


    @property
    def col(self):
        """Single column getter
        """
        return self._col

    @property
    def text(self):
        """Getter for text column
        """
        return self.data[self.col]

    @text.setter
    def text(self,series):
        """Setter for text column
        """
        self.data.loc[:,self.col] = series

    @property
    def tokens(self):
        """Getter for tokens column
        """
        return self.data["tokens"]

    @tokens.setter
    def tokens(self,series):
        """Setter for text column
        """
        self.data.loc[:,"tokens"] = series
        self.join_from_tokens()

    
    def get_flatten_text(self):
        """Get one text from all corpus
        """
        text = self.text.tolist()
        text = " ".join(text)
        return text


    def lower(self):
        """Convert the text column to lowercase
        """
        self.text = self.text.str.lower()

    def upper(self):
        """Convert the text column to uppercase
        """
        self.text = self.text.str.upper()

    def strip(self):
        """Strip the text column from trailing and leading whitespaces
        """
        self.text = self.text.str.strip()


    def map(self,func):
        """Map and modify the text column
        """
        self.text = self.text.map(func)


    def remove_unicode(self):
        """Remove all unicode characters from text column
        Example accents in French or other special characters
        """
        self.map(remove_unicode)


    def remove_punct(self):
        """Remove all punctation from text
        """
        self.map(remove_punct)


    def remove_multiple_spaces(self):
        """Remove multiple whitespaces inbetween words in the text
        """
        self.map(remove_multiple_spaces)


    def clean(self):
        """Clean text column with most uniformization functions
            - Strip
            - Lowercase
            - Remove Punctuation
            - Remove Unicode
            - Remove Multiple spaces
        """
        self.strip()
        self.lower()
        self.remove_unicode()
        self.remove_punct()
        self.remove_multiple_spaces()


    def clean_tokens(self,stopwords = None,vocab = None,min_len = 1,max_len = 30):
        """Clean tokens column
        """

        vocab = vocab if vocab is not None else []
        if stopwords is not None:
            vocab_stopwords = get_stop_words(stopwords)
            vocab.extend(vocab_stopwords)

        self.tokens = self.tokens.map(lambda x : clean_tokens(x,
            stopwords = None,
            vocab = vocab,
            min_len = min_len,
            max_len = max_len,
            ))




    def query(self):
        """Query the corpus on a condition
        Filter the corpus if inplace, returns the new corpus otherwise
        """
        pass


    def contains(self,word,inplace = True):
        """Check if a word is contained in the text
        Create a column if inplace, otherwise returns the boolean series
        """
        series = self.text.str.contains(word)
        if inplace:
            self.data[f"has_{word}"] = series
        else:
            return series


    def tokenize_sep(self,sep = " "):
        """Tokenize a corpus on a given separator
        Simplest example being splitting on whitespaces 
        """
        self.tokens = self.text.str.split(sep)


    def tokenize(self,lang = "english"):
        """Advanced tokenize function
        """
        self.tokens = self.text.map(lambda x : tokenize(x,lang))


    def join_from_tokens(self):
        """Rejoin the tokens columns into the text columns
        """
        self.text = self.tokens.map(lambda x : " ".join(x))


    def count_words_sep(self,sep = " "):
        """Simple word counter on  a separator
        """
        return (self.text.str
            .split(sep,expand = True)
            .melt()
            ["value"]
            .value_counts()
            )

    def count_words(self):
        return (self.tokens
            .apply(pd.Series)
            .melt()
            ["value"]
            .value_counts()
            )




    def detect_ngrams(self,n = 100,freq_filter = 5):
        """Detect ngrams in text and collocate them with underscore
        """
        
        # Get all list of tokens
        documents = self.tokens.tolist()

        # Get bigrams
        self.bigrams = find_bigrams(documents,freq_filter = freq_filter,n = n)

        # Replace bigrams
        self.text = self.text.map(lambda x : replace_bigrams(x,self.bigrams))









    

