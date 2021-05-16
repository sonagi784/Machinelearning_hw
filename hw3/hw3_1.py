from sklearn.preprocessing import LabelEncoder

# read "a_list.txt"
f = open("a_list.txt", 'r')
a_list = []
while True:
    line = f.readline()
    if not line: break
    a_list.append(line.split())
f.close()

# 1
le = LabelEncoder()
a_list_enc = []
for line in a_list:
    le.fit(line)
    a_list_enc.append(le.transform(line))

# write a_list_enc to "a_list_enc.txt"
f = open("a_list_enc.txt", 'w')
for line in a_list_enc:
    for l in line:
        f.write(str(l))
        f.write(' ')
    f.write('\n')
f.close()

from sklearn.preprocessing import StandardScaler
import numpy as np

# read "a_list_enc.txt"
f = open("a_list_enc.txt", 'r')
a_list_enc = []
while True:
    line = f.readline()
    if not line: break
    a_list_enc.append(line.split())
a_list_enc = np.float32(a_list_enc)
f.close()

# 2-2 (StandardScaler)
scaler = StandardScaler()
scaler.fit(np.float32(a_list_enc))
a_list_enc_norm = scaler.transform(np.float32(a_list_enc))

# write a_list_enc_norm to "a_list_enc_norm.txt"
f = open("a_list_enc_norm.txt", 'w')
for line in a_list_enc_norm:
    for l in line:
        f.write(str(l))
        f.write(' ')
    f.write('\n')
f.close()

