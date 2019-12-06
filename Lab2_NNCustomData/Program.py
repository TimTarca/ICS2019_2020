import sklearn
import pandas
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.utils import shuffle
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import cross_validate
from sklearn.preprocessing import normalize


# Timothy Tarca
# Neural Network using data about houses to determine the location of the house
# Data used is pricing, bathrooms, bedrooms, and square footage

data=pandas.read_csv("house.data", header=None)

# Graphs of the data
sns.pairplot( data=data,vars=(0,1,2,3), hue=4)
# plt.show()

# Converts the data in numpy array
data=np.array(data)
X=data[:,0:4] # This gets all the rows in only the first 4 columns.
y=data[:,4]   # Data of location the house
print(X.shape)
print(y.shape) 

# Creates the training and testing sets
X,y=shuffle(X,y,random_state=0)
print(X[:4])
X=normalize(X)
print(X[:4])
trainX=X[:75]
trainy=y[:75]
testX=X[75:]
testy=y[75:]

# Determines the number of hidden layers
# Determines the scores of the neural network
clf = MLPClassifier(hidden_layer_sizes=[4,4], random_state=0, max_iter=10000)
clf.fit(trainX, trainy)
trainScore=clf.score(trainX, trainy)
testScore=clf.score(testX, testy)
prediction=clf.predict(testX)

# Shows how accurate the neural network is at predicting the location of the house
print(clf.score(trainX,trainy))
print(clf.score(testX,testy))

# Shows cross validation results
cv_results = cross_validate(clf, X, y, cv=4)
print(cv_results)
