from sklearn import datasets

data = datasets.load_iris()

featureLabels = data.feature_names
features = data.data
targetLabels = data.target_names
target = data.target

print(featureLabels)
print(features)
print(targetLabels)
print(target)
