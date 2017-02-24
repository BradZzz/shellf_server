import numpy as np
import pandas as pd
import os

from main.lib.utils import getFiles, openFile, retUpTo
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer, TfidfTransformer
from sklearn.decomposition import PCA
from sklearn.metrics.pairwise import cosine_similarity

# Pulls in all the analyzed books in the test_assets folder
def getBooks():
    files = []
    for filename in getFiles('./data/'):
        if '.json' in filename:
            files += [filename]
    return files

def pullTerm(data, term):
    comp = []
    for x in data:
        if term in x:
            comp += [x[term]]
    return comp

def getFilename(fPath):
    return os.path.basename(fPath).replace('(analysis).json','')


class parsedBooks():
    loaded = False

    def __init__(self):
        self.datum = []
        titles = getBooks()
        for title in titles:
            data = openFile(title)
            data["raw"] = getFilename(title)
            self.datum += [data]
        self.loaded = True

    def __getDescription(self):
        contentTbl = []
        for x in self.datum:
            book = {
                'name':x['raw'],
                'google':x['meta']['google'],
            }
            contentTbl += [book]
        return contentTbl

    def getData(self):
        return self.datum

    def _genCompMap(self, df_1, df_2):
        return {
            'book1':{
                'common':df_1[df_1['word'].isin(df_2['word'])]['word'].tolist(),
                'diff':df_1[~df_1['word'].isin(df_2['word'])]['word'].tolist(),
            },
            'book2':{
                'common':df_2[df_2['word'].isin(df_1['word'])]['word'].tolist(),
                'diff':df_2[~df_2['word'].isin(df_1['word'])]['word'].tolist(),
            }
        }

    def __getKey(self, item):
        return item[0]

    def __analyzeVectorizer(self, bag):
        tfidf_vectorizer = TfidfVectorizer()
        return tfidf_vectorizer.fit_transform(bag)

    def __pca(self,vector):
        pca = PCA(n_components=2)
        pca_results = pca.fit_transform(vector)
        return pca_results

    def __coSim(self,bag):
        sim = []
        for x, matx in enumerate(bag):
            cos_sim = cosine_similarity(matx, bag)
            sim += cos_sim.tolist()
        return sim

    def __returnSelectedWords(self, wordz, selected):
        vec = CountVectorizer(analyzer = 'word')
        data = vec.fit_transform(wordz).toarray()
        dist = np.sum(data, axis=0)
        vocab = vec.get_feature_names()
        return [x for x in sorted(zip(dist, vocab), key=self.__getKey, reverse=True) if x[0] > selected]

    def compare(self, book1, book2, pos):
        df_1 = pd.DataFrame(self.__returnSelectedWords(pullTerm(self.datum,'words')[book1].split(" "), pos), columns=['count','word'])
        df_2 = pd.DataFrame(self.__returnSelectedWords(pullTerm(self.datum,'words')[book2].split(" "), pos), columns=['count','word'])
        return self._genCompMap(df_1, df_2)

    def analyze(self, pos):
        return {
            'polarity':self.datum[pos]['meta']['polarity'],
            'subjectivity':self.datum[pos]['meta']['subjectivity'],
        }

    def similarity(self):
        try:
            self.vector_words
            self.vector_sentiment
        except:
            self.vector_words = self.__coSim(self.__analyzeVectorizer(pullTerm(self.datum,'words')))
            self.vector_sentiment = self.__coSim(self.__analyzeVectorizer(pullTerm(self.datum,'sentiment')))
        return {
            'word':self.vector_words,
            'sentiment':self.vector_sentiment,
        }

    def condense(self):
        try:
            self.condensed
        except:
            self.condensed = self.similarity()
        return {
            'word': self.__pca(self.condensed['word']).tolist(),
            'sentiment': self.__pca(self.condensed['sentiment']).tolist(),
        }

    def list(self):
        return self.__getDescription()

