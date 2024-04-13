# https://www.youtube.com/watch?v=5PgqzVG9SCk

# pip install scikit-learn
# pip install pandas
# pip install numpy
# pip install pillow

import pickle
from PIL import Image, ImageOps
from io import BytesIO
import pandas as pd
import numpy as np

from sklearn.datasets import fetch_openml
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
# from sklearn.cluster import KMeans

X, y = fetch_openml('mnist_784', version=1, return_X_y=True, as_frame=True) # 28x28 = 784 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2) #random_state=42) - 20% test size
clf = RandomForestClassifier(n_jobs=-1)
clf.fit(X_train, y_train)
# print(clf.score(X_test, y_test))
# clf.predict(X_test.iloc[0:1])

# with open('model.pkl', 'wb') as f:
#     pickle.dump(clf, f)

# with open('model.pkl', 'rb') as f:
#     model = pickle.load(f)

image = Image.open("8.png").convert('L')
image = ImageOps.invert(image)
image = image.resize((28, 28))
# image.show()
img_array = np.array(image).reshape(1, -1)
prediction = clf.predict(img_array)
print(prediction)


