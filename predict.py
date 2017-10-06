#!/usr/bin/python

import pickle
import numpy
numpy.random.seed(42)


### The words (features) and authors (labels), already largely processed.
### These files should have been created from the previous (Lesson 10)
### mini-project.
words_file = "my_dataset.pkl"
labels_file = "my_feature_list.pkl"
word_data = pickle.load( open(words_file, "rb"))
labels_data = pickle.load( open(labels_file, "rb") )


count = 0
#print(word_data[:10])
for comment, label in zip(word_data, labels_data):
    count += 1
    #if comment == None:
    print(comment, label)
    #print(count)

#print(count)
### test_size is the percentage of events assigned to the test set (the
### remainder go into training)
### feature matrices changed to dense representations for compatibility with
### classifier functions in versions 0.15.2 and earlier
from sklearn import model_selection
features_train, features_test, labels_train, labels_test = model_selection.train_test_split(word_data, labels_data, test_size=0.1, random_state=42)

"""
features_train = features_train[:2]
labels_train   = labels_train[:2]
features_test = features_test[:2]
labels_test = labels_test[:2]
"""
#print(features_train[:5])
### your code goes here
from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer(sublinear_tf=True, max_df=0.5,
                             stop_words='english')

features_train = vectorizer.fit_transform(features_train[:10])
