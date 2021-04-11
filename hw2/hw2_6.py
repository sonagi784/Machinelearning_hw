from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, export_graphviz
import graphviz
import matplotlib.pyplot as plt
import numpy as np


# read "a_list_enc_disc.txt"
f = open("a_list_enc_disc.txt", 'r')
a_list_enc_disc = []
while True:
    line = f.readline()
    if not line: break
    a_list_enc_disc.append(line.split())
a_list_enc_disc = np.float32(a_list_enc_disc)
f.close()


# 6-1) split a_list_enc_disc into X_train, X_test, Y_train, Y_test 
# and run DecisionTree TWICE by changing criterion='gini' or 'entropy' 
X_data, Y_data = [], []
for line in a_list_enc_disc:
    X_data.append(line[0:-1])
    Y_data.append(line[-1].astype(int))
X_train, X_test, Y_train, Y_test = train_test_split(X_data, Y_data, test_size=0.2,random_state=33)

clf1 = DecisionTreeClassifier(criterion='gini', max_depth=10)
clf1.fit(X_train, Y_train)
clf2 = DecisionTreeClassifier(criterion='entropy', max_depth=10)
clf2.fit(X_train, Y_train)

print('gini accuracy :', clf1.score(X_test, Y_test))
print('entropy accuracy :', clf2.score(X_test, Y_test))


# 6-2) show the diagram of one decision tree using graphviz
export_graphviz(clf1, out_file='tree.dot')

with open("tree.dot") as f:
    dot_graph = f.read()
graphviz.Source(dot_graph).view()


# 6-3) run decision tree TEN TIMES by changing 'max_depth' values
clf, score = [], []
depth_list = [5, 10, 50, 100, 500, 1000, 5000, 10000, 50000, 100000]
for i in range(10):
    clf.append(DecisionTreeClassifier(max_depth=depth_list[i]))

for i in range(10):
    clf[i].fit(X_train, Y_train)

for i in range(10):
    score.append(clf[i].score(X_test, Y_test))

for i in range(10):
    print('depth', depth_list[i], 'accuracy :', score[i])


# 6-4) Plot the graph of Q 3) and find the optimal ‘max_depth’
index = np.array(['5', '10', '50', '100', '500', '1000', '5000', '10000', '50000', '100000'])
plt.bar(index, score, width=0.1, color='g')
ax = plt.subplot()
ax.set_xticks(index)
ax.set_yticks(np.arange(0.8, 1.01, 0.005))
plt.ylim(0.8, 1.0)
plt.grid(True, axis='y')
plt.xlabel('Max Depth')
plt.ylabel('Accuracy')
plt.title('6-4 Result')
plt.show()