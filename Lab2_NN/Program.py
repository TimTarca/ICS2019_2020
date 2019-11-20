import sklearn
import pandas
import matplotlib.pyplot as plt
import seaborn as sns # visualization
import numpy as np
from sklearn.utils import shuffle
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import cross_validate
from sklearn.preprocessing import normalize

# add header=None so the first row isn't ignored
data=pandas.read_csv("iris.data", header=None)

# The graphs may be used to determine which iris are harder to differentiate 
# Iris-setosa is more recognizable than the other two irises.
# Iris-vericolor and virginica have closer data points, harder to differ
sns.pairplot( data=data,vars=(0,1,2,3), hue=4)

data=np.array(data) #Change placement of this code to see what happens. May need to reorganize the whole code to make the code work
X=data[:,0:4] #This gets all the rows and only the first 4 columns.
y=data[:,4]
print(X.shape) #(150,4)
print(y.shape) #(150,)

# random_state initailizing the random number generation that will decide 
# random_state can verify that the neural network works properly
X,y=shuffle(X,y,random_state=0)
print(X[:4])
X=normalize(X)
print(X[:4])
trainX=X[:100]
trainy=y[:100]
testX=X[100:]
testy=y[100:]

clf = MLPClassifier(hidden_layer_sizes=[3,3], random_state=0, max_iter=100000)
clf.fit(trainX, trainy)
trainScore=clf.score(trainX, trainy)
testScore=clf.score(testX, testy)
prediction=clf.predict(testX)

# Shows how accurate the the neural network is at predicting the type of iris
print(clf.score(trainX,trainy))
print(clf.score(testX,testy))

cv_results = cross_validate(clf, X, y, cv=4)
print(cv_results)
