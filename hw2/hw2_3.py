from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import numpy as np

f = open("anneal.csv", 'r')
a_list = []
while True:
    line = f.readline().rstrip()
    if not line:
        break
    line = line.split(',')
    a_list.append(line)
a_list = a_list[1:-3]

for i in range(len(a_list)):
    for j in range(len(a_list[0])):
        if a_list[i][j][0] == "'":
            a_list[i][j] = str(a_list[i][j][1:-1])
f.close()

le = LabelEncoder()
a_list_enc = []
for line in a_list:
    le.fit(line)
    a_list_enc.append(le.transform(line))

scaler = StandardScaler()
scaler.fit(np.float32(a_list_enc))
a_list_enc_norm = scaler.transform(np.float32(a_list_enc))


# 3-1
X_data, Y_data = [], []
for line in a_list_enc_norm:
    X_data.append(line[0:-1])
    Y_data.append(line[-1].astype(int))

print('\n<3-1>\n')
print('a_list_enc_norm[0] \n', a_list_enc_norm[0])
print('X_data[0] \n', X_data[0])
print('Y_data[0] \n', Y_data[0])

# 3-2
X_train, X_test, Y_train, Y_test = train_test_split(X_data, Y_data, test_size=0.2,random_state=33)

print('\n<3-2>\n')
print('origin data length :', len(X_data))
print('X_train length :', len(X_train))
print('X_test length :', len(X_test))
print('Y_train length :', len(Y_train))
print('Y_test legnth :', len(Y_test))
