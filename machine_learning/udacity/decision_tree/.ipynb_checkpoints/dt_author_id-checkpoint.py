#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 3 (decision tree) mini-project.

    Use a Decision Tree to identify emails from the Enron corpus by author:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
sys.path.append("../choose_your_own/")
from email_preprocess import preprocess
from class_vis import prettyPicture, output_image


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

#########################################################
### your code goes here ###
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

t0 = time()

clf = DecisionTreeClassifier(min_samples_split=40)
# time the training 
clf.fit(features_train, labels_train)
print("Training Time:", round(time()-t0, 3), "s")

preds = clf.predict(features_test)
accuracy = accuracy_score(labels_test, preds)

print(f'Accuracy Score: {accuracy:.4f}')



#########################################################


