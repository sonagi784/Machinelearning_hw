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

a_class = set()
for i in range(len(a_list)):
    a_class.add(a_list[i][-1])
a_class = list(a_class)

# 3-3
temp = []
for cls in a_class:
    count = 0
    for i in range(len(a_list)):
        if count == 2: break
        if a_list[i][-1] == cls:
            count += 1
            temp.append(a_list[i][:-1])

for i in range(len(a_class)):
    print('class', a_class[i], temp[i], temp[i+1])
f.close()