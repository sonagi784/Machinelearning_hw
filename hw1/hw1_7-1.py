def no_of_class_values(iList, label):
    retarr = []
    
    for i in range(len(iList)):
        if label in iList[i]:
            iList[i].remove(label)
            retarr.append(iList[i])

    return retarr

print(no_of_class_values([[1, 2, 3, 4, 'A']], 'A'))
print(no_of_class_values([[1, 1, 1, 2, 'A'], [2, 4, 3, 'B'], [2, 3, 3, 3,'A']], 'A'))
print(no_of_class_values([[1, 1, 1, 2, 'A'], [2, 4, 3, 'B']], 'B'))
print(no_of_class_values([[1, 1, 1, 2, 'A'], [2, 4, 3, 'B']], 'C'))