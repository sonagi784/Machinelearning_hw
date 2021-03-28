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

#5-1
def divide_train_test(in_list, prop):
    idx = int(len(in_list) * prop)
    train_data = in_list[:idx]
    test_data = in_list[idx:]
    
    return train_data, test_data
