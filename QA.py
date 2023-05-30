import pandas as pd
import numpy as np 
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import pairwise_distances
from Preprocessing import PreProcessor



def answerQuestion(userInput):

    path = './datasets/intents.json'
    dataframe = pd.read_json(path)
    #using pandas to convert the json into tabular data for the vectorizer

    cosSimilarityThreshold = 0.15
    #lenient threshold due to a greater number of questions
    vectorizer = TfidfVectorizer(analyzer='word')

    processedInput = PreProcessor(userInput)
    X = vectorizer.fit_transform(dataframe['patterns']).toarray()
    xTrain = pd.DataFrame(X, columns = vectorizer.get_feature_names_out())
    xTest = vectorizer.transform([processedInput]).toarray()

    cosSimilarity = 1 - pairwise_distances(xTrain, xTest, metric = 'cosine')

    if cosSimilarity.max() >= cosSimilarityThreshold:
        
        argmax = np.where(cosSimilarity == np.max(cosSimilarity, axis=0))
        id = np.random.choice(argmax[0])
        return str((dataframe['response'].loc[id]))

    else:
        return ("Sorry, I didn't understand that. Could you please repeat?")
