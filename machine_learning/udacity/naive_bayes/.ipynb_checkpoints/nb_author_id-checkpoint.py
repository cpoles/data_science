#!/usr/bin/python3

"""
This is the code to accompany the Lesson 1 (Naive Bayes) mini-project.
Use a Naive Bayes Classifier to identify emails by their authors
authors and labels:
Sara has label 0
Chris has label 1
"""
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess

# features_train and features_test are the features for the training
# and testing datasets, respectively
# labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()


##############################################################
# Enter Your Code Here
from sklearn.metrics import accuracy_score
from sklearn.naive_bayes import GaussianNB

# create classifier
nb_clf = GaussianNB()

# fit classifier
nb_clf.fit(features_train, labels_train)

# predict
predictions = nb_clf.predict(features_test)

# check accuracy
accuracy = accuracy_score(labels_test, predictions)
print(f'Accuracy: {accuracy:.2f}')

##############################################################

##############################################################
'''
You Will be Required to record time for Training and Predicting
The Code Given on Udacity Website is in Python-2
The Following Code is Python-3 version of the same code
'''

t0 = time()
# # < your clf.fit() line of code >
nb_clf.fit(features_train, labels_train)
print("Training Time:", round(time()-t0, 3), "s")

t0 = time()
nb_clf.predict(features_test)
print("Predicting Time:", round(time()-t0, 3), "s")

##############################################################
