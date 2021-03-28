def no_of_class_values(iList, label):
    retarr = []
    
    for i in range(len(iList)):
        if label in iList[i]:
            iList[i].remove(label)
            retarr.append(iList[i])
    
    return retarr

#7-3
def no_of_dis_val(iList):
    
    temp = set()
    for i in range(len(iList)):
        for j in range(len(iList[0])):
            temp.add(iList[i][j])
    
    return len(set(temp))

a_list = [
    [1.1, 1.5, 0.7, 'A'],
    [0.9, 1.1, 0.2, 'A'],
    [1.5, 0.2, 0.1, 'B']
]

class_set = set()
for iList in a_list:
    class_value = iList[-1]
    class_set.add(class_value)

for class_value in class_set:
    iList = no_of_class_values(a_list, class_value)
    print(class_value, ':', no_of_dis_val(iList))



