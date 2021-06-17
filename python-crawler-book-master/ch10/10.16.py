from sklearn import svm
from sklearn import datasets

clf = svm.SVC()
iris = datasets.load_iris()

X = iris.data
y = iris.target

clf.fit(X, y)

result = clf.predict([[ 6.9, 3.1, 5.4, 2.1]])
print(result[0], iris.target_names[result[[0]]])
