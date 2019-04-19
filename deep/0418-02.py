import pandas as pd
from sklearn import svm, metrics
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier  

df = pd.read_csv("./data/mushroom.csv")  

allLabel = []
allData = []

for rowidx, row in df.iterrows():         # cf. enumerate
    allLabel.append(row.iloc[0]) 

    # 문자 -> 숫자화       
    ords = []
    for c in row.iloc[1:]:
        ords.append(ord(c))
    
    allData.append(ords)
    
trainData, testData, trainLabel, testLabel = train_test_split(allData, allLabel)

clf = RandomForestClassifier(n_estimators=100, n_jobs=6, random_state=4096)       

clf.fit(trainData, trainLabel)

pred = clf.predict(testData)
score = metrics.accuracy_score(testLabel, pred)
print("Score = ", score)
report = metrics.classification_report(testLabel, pred)
