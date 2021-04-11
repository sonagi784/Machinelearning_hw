from sklearn.preprocessing import LabelEncoder

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

# 1
le = LabelEncoder()
a_list_enc = []
for line in a_list:
    le.fit(line)
    a_list_enc.append(le.transform(line))

print(a_list_enc)