from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
import numpy as np

# read X_train, X_test, Y_train, Y_test
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
clf_neighbor = [KNeighborsClassifier(n_neighbors=1),
                KNeighborsClassifier(n_neighbors=5),
                KNeighborsClassifier(n_neighbors=9),
                KNeighborsClassifier(n_neighbors=13)]

for i in range(4):
    clf_neighbor[i].fit(X_train, Y_train)

score_neighbor = []
for i in range(4):
    score_neighbor.append(clf_neighbor[i].score(X_test, Y_test))

index = np.array(['1', '5', '9', '13'])
plt.bar(index, score_neighbor, width=0.5, color='g')
ax = plt.subplot()
ax.set_xticks(index)
ax.set_yticks(np.arange(0, 1.01, 0.05))
plt.ylim(0, 1.2)
plt.grid(True, axis='y')
plt.xlabel('Neighbor')
plt.ylabel('Accuracy')
plt.title('7-1 Result')
plt.show()


# 7-2
clf_weight = [KNeighborsClassifier(weights='uniform'), KNeighborsClassifier(weights='distance')]

for i in range(2):
    clf_weight[i].fit(X_train, Y_train)

score_weight = []
for i in range(2):
    score_weight.append(clf_weight[i].score(X_test, Y_test))

index = np.array(['uniform', 'distance'])
plt.bar(index, score_weight, width=0.5, color='g')
ax = plt.subplot()
ax.set_xticks(index)
ax.set_yticks(np.arange(0, 1.01, 0.05))
plt.ylim(0, 1.2)
plt.grid(True, axis='y')
plt.xlabel('Weight')
plt.ylabel('Accuracy')
plt.title('7-2 Result')
plt.show()


# 7-3
clf_p = [KNeighborsClassifier(p=1), KNeighborsClassifier(p=2)]

for i in range(2):
    clf_p[i].fit(X_train, Y_train)

score_p = []
for i in range(2):
    score_p.append(clf_p[i].score(X_test, Y_test))

index = np.array(['Manhattan', 'Euclidean'])
plt.bar(index, score_p, width=0.5, color='g')
ax = plt.subplot()
ax.set_xticks(index)
ax.set_yticks(np.arange(0, 1.01, 0.05))
plt.ylim(0, 1.2)
plt.grid(True, axis='y')
plt.xlabel('p')
plt.ylabel('Accuracy')
plt.title('7-3 Result')
plt.show()
