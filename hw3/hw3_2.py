from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import numpy as np

# read "a_list_enc_norm.txt"
f = open("a_list_enc_norm.txt", 'r')
a_list_enc_norm = []
while True:
    line = f.readline()
    if not line: break
    a_list_enc_norm.append(line.split())
a_list_enc_norm = np.float32(a_list_enc_norm)
f.close()

# split a_list_enc_norm into X_data and Y_data
X_data, Y_data = [], []
for line in np.float32(a_list_enc_norm):
    X_data.append(line[0:-1])
    Y_data.append(line[-1].astype(int))

# split X_data and Y_data into X_train, X_test, Y_train, Y_test
X_train, X_test, Y_train, Y_test = train_test_split(X_data, Y_data, test_size=0.2,random_state=33)

# write X_train, X_test, Y_train, Y_test
f = open("X_train.txt", 'w')
for line in X_train:
    for l in line:
        f.write(str(l))
        f.write(' ')
    f.write('\n')
f.close()

f = open("X_test.txt", 'w')
for line in X_test:
    for l in line:
        f.write(str(l))
        f.write(' ')
    f.write('\n')
f.close()

f = open("Y_train.txt", 'w')
for l in Y_train:
    f.write(str(l))
    f.write(' ')
f.close()

f = open("Y_test.txt", 'w')
for l in Y_test:
    f.write(str(l))
    f.write(' ')
f.close()

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
