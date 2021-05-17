from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn import svm
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


# 5-1) calculate the accuracy of SVC.
clf = svm.SVC()
clf.fit(X_train, Y_train)
print(clf.score(X_test, Y_test))


# 5-2) run SVC by changing kernel to ‘linear’, ‘poly’, ‘rbf’, and ‘sigmoid’, 
# and show the accuracies of each. Which kernel function shows the best accuracy ? and explain why ?
clf_kernel = []
kernels = ['linear', 'poly', 'rbf', 'sigmoid']
for k in kernels:
    clf_kernel.append(svm.SVC(kernel=k))

score_kernel = []
for i in range(len(clf_kernel)):
    clf_kernel[i].fit(X_train, Y_train)
    score_kernel.append(clf_kernel[i].score(X_test, Y_test))
print(score_kernel)

plt.bar(kernels, score_kernel, width=0.5, color='g')
ax = plt.subplot()
ax.set_xticks(kernels)
ax.set_yticks(np.arange(0, 1.01, 0.05))
plt.ylim(0, 1.2)
plt.grid(True, axis='y')
plt.xlabel('kernel')
plt.ylabel('Accuracy')
plt.title('score of SVD')
plt.show()



# 5-3) compare the accuracy of SVC with that of 
# IBL, RandomForest, and AdaBoost, respectively. Explain the results
clf = [svm.SVC(), KNeighborsClassifier(), RandomForestClassifier(), AdaBoostClassifier()]
classifiers = ['SVC', 'IBL', 'RandomForest', 'AdaBoost']

score = []
for i in range(len(classifiers)):
    clf[i].fit(X_train, Y_train)
    score.append(clf[i].score(X_test, Y_test))

print(score)
plt.bar(classifiers, score, width=0.5, color='g')
ax = plt.subplot()
ax.set_xticks(classifiers)
ax.set_yticks(np.arange(0, 1.01, 0.05))
plt.ylim(0, 1.2)
plt.grid(True, axis='y')
plt.xlabel('classifier')
plt.ylabel('Accuracy')
plt.title('score of classifier')
plt.show()