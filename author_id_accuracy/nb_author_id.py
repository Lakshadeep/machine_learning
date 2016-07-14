#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 1 (Naive Bayes) mini-project. 

    Use a Naive Bayes Classifier to identify emails by their authors
    
    authors and labels:
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()


# print features_test

#########################################################
### your code goes here ###
from sklearn.naive_bayes import GaussianNB
clf = GaussianNB()
t0 = time()
classifier = clf.fit(features_train, labels_train)
print "Training Time:", round(time()-t0, 3), "s"

t0 = time()
output = classifier.predict(features_test)
print "Prediction Time:", round(time()-t0, 3), "s"
# print output

wrong_count = 0
for i in range(len(output)):
	if(output[i] != labels_test[i]):
		wrong_count = wrong_count + 1

print "Accuracy: " + str((1 - wrong_count / 250.0) * 100)

#########################################################




