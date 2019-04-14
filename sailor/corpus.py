
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


    def __getitem__(self,key):
        if isinstance(key,int):
            return self.text.iloc[key]
        else:
            raise KeyError(f"Key {key} must be an integer")


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


    def remove_stop_words(self):
        """Remove stop words
        """
        raise NotImplementedError("Stop words removal are not yet implemented")
        self.map(remove_stop_words)


    def remove_multiple_spaces(self):
        """Remove multiple whitespaces inbetween words in the text
        """
        self.map(remove_multiple_spaces)

    def remove_short_tokens(self,size = 1):
        pass

    def remove_long_tokens(self,size = 30):
        pass

    def remove_vocab(self,vocab):
        """Remove words from text column from a given vocabulary set
        """
        pass


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
        self.data["tokens"] = self.text.str.split(sep)


    def tokenize(self):
        """Advanced tokenize function
        """
        pass


    def count_words_sep(self,sep = " "):
        """Simple word counter on  a separator
        """
        return (self.text.str
            .split(sep,expand = True)
            .melt()
            ["value"]
            .value_counts()
            )


    def detect_ngrams(self):
        """Detect ngrams in text and collocate them with underscore
        """
        pass









    

