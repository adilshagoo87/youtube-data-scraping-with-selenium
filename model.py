import prep1 as py
import pandas as pd
from sklearn import preprocessing
from sklearn.feature_extraction.text import CountVectorizer
import re 
import nltk 
from nltk.corpus import stopwords 
from nltk.stem.porter import PorterStemmer
import pickle 
df=pd.read_csv("youtubedata.csv")
df.dropna(axis=0, how="any", thresh=None, subset=None, inplace=True)                 
label_encoder = preprocessing.LabelEncoder()
df_category = label_encoder.fit_transform(df["category"].values)
print("P")
f=open("corpus.txt","r")
cor=f.read().splitlines()
f.close()
cor=cor[0]
corpus = py.corpus_build(df["title"].values)
corpus1 = py.corpus_desc(df["description"].values)
X,y =py.vector(corpus,corpus1,cor,df)
print("Q")
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state = 0)
classifier = RandomForestClassifier(n_estimators = 1000, criterion = 'entropy')
classifier.fit(X_train, y_train)
print("O")
filename = 'finalized_model2.sav'
pickle.dump(classifier, open(filename, 'wb'))
y_pred = classifier.predict(X_test)
print(classifier.score(X_test, y_test))