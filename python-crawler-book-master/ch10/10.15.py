from sklearn.cluster import KMeans
from sklearn import datasets

iris = datasets.load_iris()
X = iris.data
y = iris.target

k = KMeans(n_clusters=3)

k.fit(X)

print(X)

print(X[k.labels_ == 0, 1])
print(X[k.labels_ == 1, 1])
print(X[k.labels_ == 2, 1])
