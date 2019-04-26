#!/usr/bin/env python
# -*- coding: utf-8 -*- 


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
from tqdm import tqdm_notebook

# IO
import io
import base64
import docx2txt
import PyPDF2
import pdf2image
from PIL import Image
from wand.image import Image as Img
import pytesseract
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'


# Custom library
from ..corpus import SingleColumnCorpus



"""Requirements
- Install pytesseract correctly
- Wand
- ImageMagick
- Ghostscript
"""



def pdf_to_image(path,resolution = None,**kwargs):
    img = Img(filename=path,resolution = resolution,**kwargs)
    img_buffer = np.asarray(bytearray(img.make_blob(format='png')), dtype='uint8')
    bytesio = io.BytesIO(img_buffer)
    pil_img = Image.open(bytesio)
    return pil_img



def image_to_string(img,lang = None,**kwargs):
    return pytesseract.image_to_string(img,lang=lang,**kwargs)



def create_corpus_from_list_of_pdfs(paths,resolution = None,lang = None,**kwargs):
    # From folder
    if isinstance(paths,str):
        paths = [os.path.join(paths,x) for x in os.listdir(paths)]

    texts = []

    i = 0

    for path in tqdm_notebook(paths):
        try:
            img = pdf_to_image(path,resolution = resolution,**kwargs)
            text = image_to_string(img,lang = lang)
            texts.append({"path":path,"text":text})
        except: 
            print(f"Skipped file {path}")        
        i += 1
        if i % 10 == 0:
            pd.DataFrame(texts).to_pickle("test.pkl")

    texts = pd.DataFrame(texts)

    return texts
