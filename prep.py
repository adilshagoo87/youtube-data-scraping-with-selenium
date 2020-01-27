import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
import re 
import nltk 
from nltk.corpus import stopwords 
from nltk.stem.porter import PorterStemmer


def corpus_build(df_title,df_description):
	corpus_title = [] 
	corpus_desc = []
	for i in range(len(df_title)):         
		review = re.sub('[^a-zA-Z]', ' ', df_title[i])
		review_desc = re.sub('[^a-zA-Z]', ' ', df_description[i])     
		review, review_desc = review.lower(),review_desc.lower() 
		review, review_desc = review.split(),review_desc.split()
		ps = PorterStemmer()            
		review = [ps.stem(word) for word in review if not word in set(stopwords.words('english'))]
		review_desc = [ps.stem(word) for word in review_desc if not word in set(stopwords.words('english'))]
		review,review_desc = ' '.join(review),' '.join(review_desc) 
		corpus_title.append(review)
		corpus_desc.append(review_desc)
	return corpus_title,corpus_desc

def vector(c0,c1,df):
	cv = CountVectorizer(max_features = None) 
	X = cv.fit_transform(c0,c1).toarray()
	y = df["category"].values
	return X,y

