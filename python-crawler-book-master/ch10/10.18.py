from sklearn.model_selection import train_test_split
data = [[1, 2], [2, 3], [4, 5], [1, 2], [2, 3], [4, 5], [1, 2], [2, 3], [4, 5], [1, 2], [2, 3], [4, 5], [1, 2], [2, 3], [4, 5]]
label = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]


test_count = 3

for i in range(test_count):
    print('\n%d 번째 데이터 분리'%(i))

    X_train, X_test, y_train, y_test = train_test_split(data, label)

    print('훈련 데이터 : ', X_train)
    print('훈련 데이터 라벨 : ', X_test)
    print('테스트 데이터 : ', y_train)
    print('테스트 데이터 라벨 : ', y_test)
