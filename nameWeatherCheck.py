#functions here are used to store or change name
import nltk
from nltk import word_tokenize , sent_tokenize
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import pairwise_distances

def IsNameChange(str):
#detects if user wants to change their name
    
    path = './datasets/intents.json'
    dataframe = pd.read_json(path)
    cosSimilarityThreshold = 0.6
    
    punctuation_tokenizer = nltk.RegexpTokenizer(r"\w+")
    str = punctuation_tokenizer.tokenize(str)
    str = (" ".join(str))

    vectorizer = TfidfVectorizer(analyzer='word')
    X = vectorizer.fit_transform(dataframe['patterns']).toarray()

    xTrain = pd.DataFrame(X, columns = vectorizer.get_feature_names_out())
    xTest = vectorizer.transform([str]).toarray()

    cosSimilarity = 1 - pairwise_distances(xTrain, xTest, metric = 'cosine')

    argmax = np.where(cosSimilarity == np.max(cosSimilarity, axis=0))
    id = np.random.choice(argmax[0])

    #not only does the threshold have to exceed, but the intent has to match.
    if((cosSimilarity.max() >= cosSimilarityThreshold) and (dataframe['tag'].loc[id]) == "name_change"):
        return True
    else:
        return False

def IsWeather(str):
    path = './datasets/intents.json'
    dataframe = pd.read_json(path)
    #query = "How is the weather outside?"

    cosSimilarityThreshold = 0.6
    punctuation_tokenizer = nltk.RegexpTokenizer(r"\w+")
    str = punctuation_tokenizer.tokenize(str)
    str = (" ".join(str))

    vectorizer = TfidfVectorizer(analyzer='word')
    X = vectorizer.fit_transform(dataframe['patterns']).toarray()

    xTrain = pd.DataFrame(X, columns = vectorizer.get_feature_names_out())
    xTest = vectorizer.transform([str]).toarray()

    cosSimilarity = 1 - pairwise_distances(xTrain, xTest, metric = 'cosine')

    argmax = np.where(cosSimilarity == np.max(cosSimilarity, axis=0))
    id = np.random.choice(argmax[0])
    
    if((cosSimilarity.max() >= cosSimilarityThreshold) and (dataframe['tag'].loc[id]) == "weather"):
        return True
    else:
        return False

