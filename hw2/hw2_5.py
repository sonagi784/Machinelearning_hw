from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import KBinsDiscretizer
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

disc = KBinsDiscretizer(n_bins=4, encode='ordinal', strategy='uniform')
disc.fit(np.float32(a_list_enc))
a_list_enc_disc = disc.transform(np.float32(a_list_enc))

print(a_list_enc[0])
print(a_list_enc_disc[0])
