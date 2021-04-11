from sklearn.preprocessing import KBinsDiscretizer
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

# 5-1) discretize the attribute with N=4 intervals
disc = KBinsDiscretizer(n_bins=4, encode='ordinal', strategy='uniform')
disc.fit(np.float32(a_list_enc))
a_list_enc_disc = disc.transform(np.float32(a_list_enc))

# write a_list_enc_disc to "a_list_enc_disc.txt"
f = open("a_list_enc_disc.txt", 'w')
for line in a_list_enc_disc:
    for l in line:
        f.write(str(l))
        f.write(' ')
    f.write('\n')
f.close()

print(a_list_enc_disc)