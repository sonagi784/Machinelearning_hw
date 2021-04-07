def min_max_avg_med(iList):
    minnum = min(iList)
    maxnum = max(iList)
    avgnum = sum(iList) / len(iList)
    mednum = list(sorted(iList))[len(iList)//2]
    
    return [minnum, maxnum, avgnum, mednum]


iList = [1, 5, 3, 10, 4]
print(min_max_avg_med(iList))