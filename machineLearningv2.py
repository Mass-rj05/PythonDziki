import pandas as pd
import sys
import scipy
import numpy as np
import matplotlib
import pandas
import pandas
import sklearn
#wczytanie bibliotek
from pandas import read_csv
from pandas.plotting import scatter_matrix
from matplotlib import pyplot
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC


#Wczytanie danych z pliku
df = pd.read_csv ('exportDataframe.csv')   #read the csv file (put 'r' before the path string to address any special characters in the path, such as '\'). Don't forget to put the file name at the end of the path + ".csv"

#print(df.describe())


scatter_matrix(df)

#pyplot.show()
#df['Routes total'] = df['Routes total'].values.toint

#print(df)
# Split-out validation dataset
print(df)
dfc= df['Routes total'].astype(float)
print(type(dfc))
array = dfc.values
X = array[:,  :1]



X = np.around(X, decimals = 0)
print(X)
Y = array[:,0]
Y = np.around(Y, decimals = 3)

#print(Y)
#print(type(Y))
=======






X_train, X_validation, Y_train, Y_validation = train_test_split(X, Y, test_size=0.20, random_state=1)

models = []
models.append(('LR', LogisticRegression(solver='liblinear', multi_class='ovr')))
models.append(('LDA', LinearDiscriminantAnalysis()))
models.append(('KNN', KNeighborsClassifier()))
models.append(('CART', DecisionTreeClassifier()))
models.append(('NB', GaussianNB()))
models.append(('SVM', SVC(gamma='auto')))
# evaluate each model in turn
results = []
names = []


