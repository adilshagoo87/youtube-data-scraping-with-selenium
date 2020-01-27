import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
import re 
import nltk 
from nltk.corpus import stopwords 
from nltk.stem import WordNetLemmatizer
wordnet_lematizer=WordNetLemmatizer()


def corpus_build(df_title):
	corpus = []
	t1 = []
	for i in range(len(df_title)):         
		review = re.sub('[^a-zA-Z]', ' ', df_title[i])            
		review = review.lower()            
		tokenization=nltk.word_tokenize(review)
		for j in tokenization:
			t1.append(wordnet_lematizer.lemmatize(j))            
		review = [word for word in t1 if not word in set(stopwords.words('english'))]            
		review = ' '.join(review) 
		print(review)
		corpus.append(review)
	return corpus
print("Y")

def corpus_desc(df_description):
	corpus1 = [] 
	t2 =[]
	for i in range(len(df_description)):            
		review = re.sub('[^a-zA-Z]', ' ', df_description[i])            
		review = review.lower()            
		tokenization=nltk.word_tokenize(review)
		for j in tokenization:
			t2.append(wordnet_lematizer.lemmatize(j))            
		review = [word for word in t2 if not word in set(stopwords.words('english'))]            
		review = ' '.join(review)
		print(review)
		corpus1.append(review)
	return corpus1
print("X")
def vector(corpus,corpus1,cor,df):
	for i in range(len(corpus)):
		corpus[i]=corpus[i]+corpus1[i]+cor
	cv = CountVectorizer(max_features = 1500) 
	X = cv.fit_transform(corpus).toarray()
	y = df["category"].values
	return X,y
print("z")

