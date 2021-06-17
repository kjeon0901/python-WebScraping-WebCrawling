from sklearn.cluster import KMeans
from sklearn import datasets

iris = datasets.load_iris()
X = iris.data
# y = iris.target 클러스터링은 학습시킬 때 라벨을 포함시키지 않습니다.

k = KMeans(n_clusters=3)

k.fit(X)

print(X)
print('군집화 시킨 후 라벨')
print(k.labels_)
print('답')
print(iris.target)
