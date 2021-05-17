import numpy as np
import matplotlib.pyplot as plt
from sklearn.mixture import GaussianMixture

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

# 7-1
gmm = []
estimators = [2, 3, 7]
for i in range(len(estimators)):
    gmm.append(GaussianMixture(n_components=estimators[i]))
    gmm[i].fit(X_train)
print(gmm)


# 7-2
gmm = GaussianMixture(n_components=3)
gmm.fit(X_train, Y_train)
labels = gmm.predict(X_test)
print(labels)


# 7-3
probs = gmm.predict_proba(X_train)
print(probs.round(3)) 