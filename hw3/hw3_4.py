from sklearn.ensemble import RandomForestClassifier
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

# 4-1) Run by changing n_estimators = 2, 5, 30, 50, 100, respectively, and show the accuracies of each run
clf = []
estimators = [2, 5, 30, 50, 100]
for estimator in estimators:
    clf.append(RandomForestClassifier(n_estimators=estimator))

score_RandomForest = []
for i in range(len(clf)):
    clf[i].fit(X_train, Y_train)
    score_RandomForest.append(clf[i].score(X_test, Y_test))
print(score_RandomForest)

# 4-2) Plot your results and explain the effect of the n_estimators
index = np.array(['2', '5', '30', '50', '100'])
plt.bar(index, score_RandomForest, width=0.5, color='g')
ax = plt.subplot()
ax.set_xticks(index)
ax.set_yticks(np.arange(0, 1.01, 0.05))
plt.ylim(0, 1.2)
plt.grid(True, axis='y')
plt.xlabel('n_estimators')
plt.ylabel('Accuracy')
plt.title('Accuracy of RandomForestClassifier')
plt.show()


# 4-3) Choose the optimal n_estimators from q. 1), 
# and run the model by changing oob_score = True/False. respectively. 
# Show the accuracies of each run, and explain the effect of the oob_score.

optimal_idx = score_RandomForest.index(max(score_RandomForest))
optimal_estimator = estimators[optimal_idx]

clf_oob = []
clf_oob.append(RandomForestClassifier(n_estimators=estimator, oob_score=True))
clf_oob.append(RandomForestClassifier(n_estimators=estimator, oob_score=False))

score_oob = []
for i in range(len(clf_oob)):
    clf_oob[i].fit(X_train, Y_train)
    score_oob.append(clf_oob[i].score(X_test, Y_test))

index = np.array(['True', 'False'])
plt.bar(index, score_oob, width=0.5, color='g')
ax = plt.subplot()
ax.set_xticks(index)
ax.set_yticks(np.arange(0, 1.01, 0.05))
plt.ylim(0, 1.2)
plt.grid(True, axis='y')
plt.xlabel('bool')
plt.ylabel('Accuracy')
plt.title('Accuracy of oob_score')
plt.show()


# 4-4) Choose the optimal n_estimators from q. 1), 
# and run the model by changing max_features = “auto”, “sqrt”, “log2”, respectively. 
# Show the accuracies of each run, and explain the effect of the max_features.

optimal_idx = score_RandomForest.index(max(score_RandomForest))
optimal_estimator = estimators[optimal_idx]

clf_features = []
clf_features.append(RandomForestClassifier(n_estimators=estimator, max_features="auto"))
clf_features.append(RandomForestClassifier(n_estimators=estimator, max_features="sqrt"))
clf_features.append(RandomForestClassifier(n_estimators=estimator, max_features="log2"))

score_features = []
for i in range(len(clf_features)):
    clf_features[i].fit(X_train, Y_train)
    score_features.append(clf_features[i].score(X_test, Y_test))

index = np.array(['auto', 'sqrt', 'log2'])
plt.bar(index, score_features, width=0.5, color='g')
ax = plt.subplot()
ax.set_xticks(index)
ax.set_yticks(np.arange(0, 1.01, 0.05))
plt.ylim(0, 1.2)
plt.grid(True, axis='y')
plt.xlabel('features')
plt.ylabel('Accuracy')
plt.title('Accuracy of max_features')
plt.show()
