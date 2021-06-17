from sklearn.cluster import KMeans
from sklearn import datasets
import matplotlib.pyplot as plt

iris = datasets.load_iris()
X = iris.data
y = iris.target

k = KMeans(n_clusters=3)

k.fit(X)

for target_name_index in range(len(iris.target_names)):
    if target_name_index == 0:
        c = 'r'
        marker = '>'
    elif target_name_index == 1:
        c = 'g'
        marker = 'o'
    elif target_name_index == 2:
        c = 'b'
        marker = 'x'

    plt.figure('k-means 결과')
    plt.scatter(X[k.labels_ == target_name_index, 0],
                X[k.labels_ == target_name_index, 1],
                marker=marker,
                c=c)

    plt.figure('원래 답')
    plt.scatter(X[y == target_name_index, 0],
                X[y == target_name_index, 1],
                marker=marker,
                c=c)

plt.show()
