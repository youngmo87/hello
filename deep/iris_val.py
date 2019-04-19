from sklearn import svm, metrics
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score

csv = pd.read_csv('./data/iris.csv')       # csv[:4] : 0 ~ 4행
cdata = csv[['SepalLength', 'SepalWidth', 'PetalLength', 'PetalWidth']]
cret = csv['Name']

trainData, testData, trainLabel, testLabel = train_test_split(cdata, cret)
print(trainData, trainLabel)

clf = svm.SVC(gamma='auto')  
clf.fit(trainData, trainLabel)
pred = clf.predict(testData)

kscores = cross_val_score(clf, cdata, cret, cv = 10)
score = metrics.accuracy_score(testLabel, pred)

print("Score=", score)
print("Kscore=", kscores)