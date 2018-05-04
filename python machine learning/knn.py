from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import numpy as np

# CSV_DATA = pd.read_csv('iris.csv').as_matrix()
# dataset = np.array(CSV_DATA[:,:5])
# np.random.shuffle(dataset)
#
# train_data = np.array(dataset[:100,:4])
# train_label = np.array(dataset[:100,4])
#
# test_data = np.array(dataset[100:,:4])
# test_label = np.array(dataset[100:,4])
#
# classifier = KNeighborsClassifier(n_neighbors=5)
# classifier.fit(train_data,train_label)
#
# result = classifier.score(test_data,test_label)
#
# print(result)

csv_data = pd.read_csv('test.csv').as_matrix()
dataset = np.array(csv_data)
train_data = np.array(dataset[:,:2])
train_label = np.array(dataset[:,2])

clf = KNeighborsClassifier(n_neighbors=3)
clf.fit(train_data,train_label)

print(clf.predict([[100,100],[20,20]]))