#!/usr/bin/python

import matplotlib.pyplot as plt
from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture

features_train, labels_train, features_test, labels_test = makeTerrainData()


### the training data (features_train, labels_train) have both "fast" and "slow"
### points mixed together--separate them so we can give them different colors
### in the scatterplot and identify them visually
grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==0]
bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==0]
grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==1]
bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==1]


#### initial visualization
plt.xlim(0.0, 1.0)
plt.ylim(0.0, 1.0)
plt.scatter(bumpy_fast, grade_fast, color = "b", label="fast")
plt.scatter(grade_slow, bumpy_slow, color = "r", label="slow")
plt.legend()
plt.xlabel("bumpiness")
plt.ylabel("grade")
plt.show()
################################################################################


### your code here!  name your classifier object clf if you want the 
### visualization code (prettyPicture) to show you the decision boundary

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

params = {'bootstrap': False,
 'criterion': 'entropy',
 'max_depth': 7,
 'max_features': 'auto',
 'max_leaf_nodes': 16,
 'n_estimators': 200,
 'n_jobs': -1,
 'oob_score': False}


clf = RandomForestClassifier(**params)

clf.fit(features_train, labels_train)


y_pred_rf = clf.predict(features_test)
print(accuracy_score(labels_test, y_pred_rf))


try:
    prettyPicture(clf, features_test, labels_test)
except NameError:
    pass
