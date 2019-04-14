

from langdetect import detect




def detect_language(x):
    return detect(x)




    # def translate(self,to = "english",inplace = True,with_deepl = True):
    #     """
    #     Translate the text of the document
    #     """

    #     if with_deepl:
    #         nltk_lang = to
    #         deepl_lang = LANGUAGES_NLTK_BLOBDEEPL[nltk_lang].upper()
    #         translation = pydeepl.translate(self.text, deepl_lang)

    #     else:
    #         nltk_lang = to
    #         blob_lang = LANGUAGES_NLTK_BLOBDEEPL[nltk_lang]
    #         translation = TextBlob(self.text).translate(to = blob_lang).raw

    #     if inplace:
    #         self.set_text(translation)
    #     else:
    #         return translation


