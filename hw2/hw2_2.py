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