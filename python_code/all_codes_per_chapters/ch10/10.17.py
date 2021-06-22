from sklearn import svm, metrics
from sklearn import datasets
from sklearn.model_selection import train_test_split

clf = svm.SVC()
iris = datasets.load_iris()

X = iris.data
y = iris.target

# 기존 데이터를 훈련 데이터와 테스트 데이터로 분리
X_train, X_test, y_train, y_test = train_test_split(X, y)

# 훈련 데이터를 학습
clf.fit(X_train, y_train)

# 테스트 데이터 예측
predict_result = clf.predict(X_test)

# 테스트 데이터와 예측된 데이터 라벨 비교
score = metrics.accuracy_score(y_test, predict_result)
report = metrics.classification_report(y_test, predict_result)

print('정답률 : ', score)
print('보고서 : ', report)
