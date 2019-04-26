![](https://i.ibb.co/R6G65pW/logo1.png)
![](https://i.ibb.co/f2qW1mP/banner1.png)

A Python library wrapping many NLP tasks on a corpus

# Sailor NLP in a nutshell
> There are plenty of NLP libraries in Python, yet most of them (spaCy, NLTK, Textblob) are dedicated to single text analysis. <br>
> When you have to extract information from a corpus of texts or documents you always need to reinvent the wheel.<br>
> That's when the **Sailor** comes in ! To guide and help you explore unstructured text corpuses. <br>
> The goal is not create state-of-the-art NER or POS-tagging model, but to wrap plenty of functionalities from topic extraction to supervised learning.<br>

## Use cases
Anything that has multiple texts:
- Set of reviews or comments
- Set of articles
- Set of tweets

## What can you do with Sailor ?
- Unsupervised learning (Clustering)
- Unsupervised mining (Topic extraction)
- Supervised learning (Classification)
- Supervised mining (Interpretability, Universe extraction)
- Corpus modelling (Doc2Vec)
- Visualizations
- IO (from OCR)

## How is it different than other libraries ?
Sailor's goal is simplicity of use. <br> 
It was built for non NLP practicioners that don't know how to use SpaCy or complex language models, but just want to analyze very fast short corpuses of texts. <br>
That's why the core of Sailor is just extending Pandas DataFrames to text analysis for fast processing and ease of use. 
Over time it will include other advanced functionalities like Deep Learning through SpaCy, flair, or Fast.ai.



# Requirements
```
nltk.download('punkt')
nltk.download('stopwords')
```


