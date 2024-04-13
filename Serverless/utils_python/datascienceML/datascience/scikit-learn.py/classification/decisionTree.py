
# https://www.youtube.com/watch?v=7eh4d6sabA0&list=TLPQMDEwNDIwMjRa98HwKeIcjQ&index=7

# pip install scikit-learn==1.4.2
# pip install pandas==2.2.2
# pip install numpy==1.26.4

import pandas as pd
import numpy as np

from sklearn.utils._bunch import Bunch
# from sklearn.datasets import fetch_openml, load_iris, load_breast_cancer, load_digits, load_wine, load_diabetes
# from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
# from sklearn.cluster import KMeans
# from sklearn.svm import SVC
# from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
# import joblib


# bunch:Bunch = load_wine()
# print(type(bunch)) # bunch

# bunch = load_wine()
# print(type(bunch)) # bunch

# X, y = load_wine(return_X_y=True)
# print(type(X), type(y)) # ndarray, ndarray

# X, y = load_wine(return_X_y=True, as_frame=True)
# print(type(X), type(y)) # dataframe, series
# print(X.describe())


df = pd.read_csv("sampledata/music.csv")
# df
# df.shape
# df.values
# df.head(3)
# df.describe()
# df.plot()
X = df.drop(columns=["genre"]) # does not modify original
y = df["genre"] # select genre column

model = DecisionTreeClassifier()

# model.fit(X, y)
# model.score(X, y) # 1.0
# predictions = model.predict( [ [21, 1], [22, 0] ] )
# predictions # array(['HipHop', 'Dance'], dtype=object)

# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2) #random_state=42) - 20% test size
# model.fit(X_train, y_train)
# predictions = model.predict(X_test)
# score = accuracy_score(y_test, predictions)
# score

# joblib.dump(model, "music-recommender.joblib")
# model = joblib.load("music-recommender.joblib")

# Visualization - Install a graphviz dot VSCode extension, command Graphviz
model.fit(X, y)
# tree.export_graphviz(model, out_file="music-recommender.dot", feature_names=X.columns, class_names=np.unique(y), filled=True)
tree.export_graphviz(   model, 
                        out_file="music-recommender.dot", 
                        feature_names=X.columns, 
                        class_names=sorted(np.unique(y)),
                        rounded=True, 
                        filled=True
                    )
