from sklearn.neural_network import MLPClassifier
from matplotlib import pyplot as plt
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

# 4-1
clf1 = [MLPClassifier(hidden_layer_sizes=(10,), max_iter=200), 
        MLPClassifier(hidden_layer_sizes=(20,), max_iter=200), 
        MLPClassifier(hidden_layer_sizes=(30,), max_iter=200)]
clf2 = [MLPClassifier(hidden_layer_sizes=(10, 10), max_iter=200), 
        MLPClassifier(hidden_layer_sizes=(20, 20), max_iter=200), 
        MLPClassifier(hidden_layer_sizes=(30, 30), max_iter=200)]

for i in range(3):
    clf1[i].fit(X_train, Y_train)
    clf2[i].fit(X_train, Y_train)

score1 = [clf1[0].score(X_test, Y_test), clf1[1].score(X_test, Y_test), clf1[2].score(X_test, Y_test)]
score2 = [clf2[0].score(X_test, Y_test), clf2[1].score(X_test, Y_test), clf2[2].score(X_test, Y_test)]
print(score1, score2)

# 4-2
index = np.array([10, 20, 30])
plt.bar(index-1, score1, width=2, color='r')
plt.bar(index+1, score2, width=2, color='b')
ax = plt.subplot()
ax.set_xticks(index)
ax.set_yticks(np.arange(0, 1.01, 0.05))
plt.ylim(0, 1.2)
plt.grid(True, axis='y')
plt.xlabel('The number of hidden nodes')
plt.ylabel('Accuracy')
plt.title('4-2 Result')
plt.legend(['One hidden layer', 'Two hidden layer'])
plt.show()

# 4-3
clf_activation = [MLPClassifier(hidden_layer_sizes=(20,), max_iter=200, activation='identity'), 
                MLPClassifier(hidden_layer_sizes=(20,), max_iter=200, activation='logistic'),
                MLPClassifier(hidden_layer_sizes=(20,), max_iter=200, activation='tanh'), 
                MLPClassifier(hidden_layer_sizes=(20,), max_iter=200, activation='relu')]

for i in range(4):
    clf_activation[i].fit(X_train, Y_train)

score_activation = [clf_activation[0].score(X_test, Y_test), clf_activation[1].score(X_test, Y_test), clf_activation[2].score(X_test, Y_test), clf_activation[3].score(X_test, Y_test)]
print(score_activation)

index = np.array(['identity', 'logistic', 'tanh', 'relu'])
plt.bar(index, score_activation, width=0.4, color='g')
ax = plt.subplot()
ax.set_xticks(index)
ax.set_yticks(np.arange(0, 1.01, 0.05))
plt.ylim(0, 1.2)
plt.grid(True, axis='y')
plt.xlabel('Activation Function')
plt.ylabel('Accuracy')
plt.title('4-3 Result')
plt.show()


# 4-4
clf_momentum = [MLPClassifier(hidden_layer_sizes=(20,), max_iter=200, momentum=0.0), 
                MLPClassifier(hidden_layer_sizes=(20,), max_iter=200, momentum=0.2),
                MLPClassifier(hidden_layer_sizes=(20,), max_iter=200, momentum=0.4), 
                MLPClassifier(hidden_layer_sizes=(20,), max_iter=200, momentum=0.6),
                MLPClassifier(hidden_layer_sizes=(20,), max_iter=200, momentum=0.8)]

for i in range(5):
    clf_momentum[i].fit(X_train, Y_train)

score_momentum = [clf_momentum[0].score(X_test, Y_test), clf_momentum[1].score(X_test, Y_test), clf_momentum[2].score(X_test, Y_test),
                clf_momentum[3].score(X_test, Y_test), clf_momentum[4].score(X_test, Y_test)]
print(score_momentum)

index = np.array([0.0, 0.2, 0.4, 0.6, 0.8])
plt.bar(index, score_momentum, width=0.1, color='g')
ax = plt.subplot()
ax.set_xticks(index)
ax.set_yticks(np.arange(0, 1.01, 0.05))
plt.ylim(0, 1.2)
plt.grid(True, axis='y')
plt.xlabel('Momentum')
plt.ylabel('Accuracy')
plt.title('4-4 Result')
plt.show()


# 4-5
clf_learning = [MLPClassifier(hidden_layer_sizes=(20,), max_iter=200, learning_rate='constant', learning_rate_init=0.001),
                MLPClassifier(hidden_layer_sizes=(20,), max_iter=200, learning_rate='constant', learning_rate_init=0.01),
                MLPClassifier(hidden_layer_sizes=(20,), max_iter=200, learning_rate='invscaling', learning_rate_init=0.001),
                MLPClassifier(hidden_layer_sizes=(20,), max_iter=200, learning_rate='invscaling', learning_rate_init=0.01)]

for i in range(4):
    clf_learning[i].fit(X_train, Y_train)

score_learning = [clf_learning[0].score(X_test, Y_test), clf_learning[1].score(X_test, Y_test), clf_learning[2].score(X_test, Y_test), clf_learning[3].score(X_test, Y_test)]
print(score_learning)

index = np.array(['constant(0.001)', 'constant(0.01)', 'invscaling(0.001)', 'invscaling(0.01)'])
plt.bar(index, score_learning, width=0.5, color='g')
ax = plt.subplot()
ax.set_xticks(index)
ax.set_yticks(np.arange(0, 1.01, 0.05))
plt.ylim(0, 1.2)
plt.grid(True, axis='y')
plt.xlabel('Learning Rate')
plt.ylabel('Accuracy')
plt.title('4-5 Result')
plt.show()