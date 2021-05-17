from sklearn import cluster
from sklearn.cluster import KMeans
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


# 6-1) run KMeans 3 times by changing n_clusters = 2, 5, 7 respectively and show the mean of each cluster.
X = X_train[:, :2]
Y = Y_train

for c in [2, 5, 7]:
    kmeans = KMeans(n_clusters=c)
    kmeans.fit(X)
    
    plt.scatter(X[:, 0], X[:, 1], marker='o', s=10, c='b')
    plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], marker='s', s=50, c='r')
    plt.show()


# 6-2) For the clustering of k=2, pick one cluster. Calculate the average value of each attribute of the data in that cluster. 
kmeans = KMeans(n_clusters=2)
kmeans.fit(X)
print('\n< average value >')
print(kmeans.inertia_ / (len(X)//2))


# 6-3) For each cluster, calculate majority (the most frequent) value of class/target value. (let’s call this ‘cluster label’)
def most_frequent(List):
    List = List.tolist()
    return max(set(List), key = List.count)


kmeans = KMeans(n_clusters=2)
kmeans.fit(X)
cluster_label = most_frequent(kmeans.labels_)
print('\n< cluster label >')
print(cluster_label)


# 6-4) Suppose each of X_test is classified based on ‘cluster labels’, calculate the accuracy.
test = kmeans.predict(X_test[:, :2])
acc = 0
for tmp in test:
    if tmp == cluster_label:
        acc += 1
cluster_acc = (acc / len(test)) * 100
print('\n< X_test accuracy >')
print(cluster_acc)


# 6-5) run KMeans 3 times by changing n_init values (your own choice of n_init). Compare the performance of each.
print('\n< n_init = 10 20 30 >')
init_nums = [10, 20, 30]
for n in init_nums:
    kmeans = KMeans(n_init = n)
    kmeans.fit(X)
    
    test = kmeans.predict(X_test[:, :2])
    acc = 0
    for i in range(len(test)):
        if test[i] == Y_test[i]:
            acc += 1
    cluster_acc = (acc / len(test)) * 100
    print(cluster_acc)
