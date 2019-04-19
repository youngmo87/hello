from sklearn import svm, metrics
import pandas as pd

xor_data = [
    [0, 0, 0],
    [0, 1, 1],
    [1, 0, 1],
    [1, 1, 0]
    ]

df = pd.DataFrame(xor_data)

# print(df.shape)
# print("head=", df.head)
# print("colums=", list(df.columns))

#파이썬은 ":"을 써주어야 한다. R과 달리..
# print(df.loc[:, 0:1])

clf = svm.SVC(gamma='auto')
clf.fit(df.loc[:, 0:1], df.loc[:, 2])

pred = clf.predict([[0, 1], [1, 0], [1, 1], [2, -1]])
print("pred=", pred)

score = metrics.accuracy_score([1,1,0, 1], pred)
print("score=", score[1])

while True:
    cmd = input("Input x y >>")
    