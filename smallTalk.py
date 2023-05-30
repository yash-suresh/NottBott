import pandas as pd
import numpy as np 
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import pairwise_distances


def IsSmallTalk(str):
#detects if the user is attempting smalltalk
    
    path = './datasets/smallTalk.json'
    dataframe = pd.read_json(path)
    cosineSimilarityThreshold = 0.7
    #set after testing. needs to equal or exceed this if it is Small Talk

    vectorizer = TfidfVectorizer(analyzer='word')
    X = vectorizer.fit_transform(dataframe['patterns']).toarray()
    xTrain = pd.DataFrame(X, columns = vectorizer.get_feature_names_out())
    xTest = vectorizer.transform([str]).toarray()

    cosSimilarity = 1 - pairwise_distances(xTrain, xTest, metric = 'cosine')

    argmax = np.where(cosSimilarity == np.max(cosSimilarity, axis=0))
    id = np.random.choice(argmax[0])
    #finding the array location in the dataframe where cosSimilarity is max.
        
    return cosSimilarity.max() >= cosineSimilarityThreshold


def returnSmallTalk(str):
#if small talk, return an appropriate response

    path = './datasets/smallTalk.json'
    dataframe = pd.read_json(path)
    
    vectorizer = TfidfVectorizer(analyzer='word')
    X = vectorizer.fit_transform(dataframe['patterns']).toarray()
    xTrain = pd.DataFrame(X, columns = vectorizer.get_feature_names_out())
    xTest = vectorizer.transform([str]).toarray()
    cosSimilarity = 1 - pairwise_distances(xTrain, xTest, metric = 'cosine')

    argmax = np.where(cosSimilarity == np.max(cosSimilarity, axis=0))
    id = np.random.choice(argmax[0])
    #finding the array location in the dataframe where cosSimilarity is max.

    return (dataframe['response'].loc[id])



    





