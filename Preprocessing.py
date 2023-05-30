import nltk
from nltk import word_tokenize , sent_tokenize
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer

stop_words = set(stopwords.words('english'))
snow_stemmer = SnowballStemmer(language='english')



def PreProcessor(str):
    punctuation_tokenizer = nltk.RegexpTokenizer(r"\w+")
    tokenisedString = punctuation_tokenizer.tokenize(str)
    #we can tokenize and remove punctuation using these two expression
    # we can also manipulate the regex depending on how we want to tokenise
    loweredString = []
    #need to convert everything to lower case first
    for word in tokenisedString:
        word = word.lower()
        loweredString.append(word)
    
    filteredString = []
    #need to filter through and remove stopwords

    for word in loweredString:
        if word not in stop_words:
            filteredString.append(word)

    stemmedWordsList = []
    
    for word in filteredString:
        stemWord =snow_stemmer.stem(word)
        stemmedWordsList.append(stemWord)
        
    del filteredString
    del loweredString
    del tokenisedString
    #remove unnecessary intermediate variables (artefacts) produced along the way.
    
    return (" ".join(stemmedWordsList))