from sklearn import svm, metrics
import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV


csv = pd.read_csv('./data/iris.csv')       # csv[:4] : 0 ~ 4행
cdata = csv[['SepalLength', 'SepalWidth', 'PetalLength', 'PetalWidth']]
cret = csv['Name']

trainData, testData, trainLabel, testLabel = train_test_split(cdata, cret)
# print(trainData, trainLabel)

clf = svm.SVC(gamma='auto')  
clf.fit(trainData, trainLabel)
pred = clf.predict(testData)
score = metrics.accuracy_score(testLabel, pred)


params = [
    {"C": [1, 10, 100, 1000], "kernel": ['linear']},
    {"C": [1, 10, 100, 1000], "kernel": ['rbf'], "gamma": [0.001, 0.0001]},
]

clf = GridSearchCV(svm.SVC(), params, n_jobs = -1, cv = 3, iid=True)

# clf = svm.SVC(gamma='auto')   # old training
clf.fit(train['images'], train['images'])


print("machine=", clf.best_estimator_)
print("Score=", score)
