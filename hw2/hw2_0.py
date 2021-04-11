# read "anneal.csv"
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

# write a_list to "a_list.txt"
f = open("a_list.txt", 'w')
for line in a_list:
    for l in line:
        f.write(l)
        f.write(' ')
    f.write('\n')
f.close()

# read "a_list.txt"
f = open("a_list.txt", 'r')
a_list = []
while True:
    line = f.readline()
    if not line: break
    a_list.append(line.split())
f.close()

print(a_list)