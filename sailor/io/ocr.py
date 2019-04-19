#!/usr/bin/env python
# -*- coding: utf-8 -*- 


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os

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


