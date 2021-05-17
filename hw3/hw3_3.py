from sklearn.ensemble import AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
import numpy as np

# prepare X_train, X_test, Y_train, Y_test
f = open("X_train.txt", 'r')
X_train = []
while True:
    line = f.readline()
    if not line: break
    X_train.append(line.split())
X_train = np.float32(X_train)
f.close()

f = open("X_test.txt", 'r')
X_test = []
while True:
    line = f.readline()
    if not line: break
    X_test.append(line.split())
X_test = np.float32(X_test)
f.close()

f = open("Y_train.txt", 'r')
line = f.readline()
Y_train = list(map(int, line.split()))
f.close()

f = open("Y_test.txt", 'r')
line = f.readline()
Y_test = list(map(int, line.split()))
f.close()

# 3-1) run by changing n_estimators and show the accuracies of each run
clf = []
estimators = [5, 7, 10, 30, 100]
for estimator in estimators:
    clf.append(AdaBoostClassifier(n_estimators=estimator))

predictions = []
pred_prob = []
score_AdaBoost = []
for i in range(len(clf)):
    clf[i].fit(X_train, Y_train)
    predictions.append(clf[i].predict(X_test))
    pred_prob.append(clf[i].predict_proba(X_test))
    score_AdaBoost.append(clf[i].score(X_test, Y_test))
print(score_AdaBoost)

# 3-2) plot your results and explain the effect of the n_estimators.
index = np.array(['5', '7', '10', '30', '100'])
plt.bar(index, score_AdaBoost, width=0.5, color='g')
ax = plt.subplot()
ax.set_xticks(index)
ax.set_yticks(np.arange(0, 1.01, 0.05))
plt.ylim(0, 1.2)
plt.grid(True, axis='y')
plt.xlabel('n_estimators')
plt.ylabel('Accuracy')
plt.title('score of AdaBoostClassifier')
plt.show()


# 3-3) compare the best performance of AdaBoostClassifier with that of IBL
clf_neighbor = [KNeighborsClassifier(n_neighbors=1),
                KNeighborsClassifier(n_neighbors=5),
                KNeighborsClassifier(n_neighbors=9),
                KNeighborsClassifier(n_neighbors=13)]
for i in range(4):
    clf_neighbor[i].fit(X_train, Y_train)
score_neighbor = []
for i in range(4):
    score_neighbor.append(clf_neighbor[i].score(X_test, Y_test))

clf_weight = [KNeighborsClassifier(weights='uniform'), KNeighborsClassifier(weights='distance')]
for i in range(2):
    clf_weight[i].fit(X_train, Y_train)
score_weight = []
for i in range(2):
    score_weight.append(clf_weight[i].score(X_test, Y_test))

clf_p = [KNeighborsClassifier(p=1), KNeighborsClassifier(p=2)]
for i in range(2):
    clf_p[i].fit(X_train, Y_train)
score_p = []
for i in range(2):
    score_p.append(clf_p[i].score(X_test, Y_test))

print('\n<Best Performance of AdaBoostClassifier>')
print(max(score_AdaBoost), end='\n\n')

print('<Best Performance of IBL>')
print(max(max(score_neighbor), max(score_weight), max(score_p)))