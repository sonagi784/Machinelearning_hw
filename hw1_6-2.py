def min_max_avg_med(iList):
    minnum = min(iList)
    maxnum = max(iList)
    avgnum = sum(iList) / len(iList)
    mednum = list(sorted(iList))[len(iList)//2]
    
    return [minnum, maxnum, avgnum, mednum]

#6-2
import random

iList = [random.randrange(-9, 10) for _ in range(10)]

print(min_max_avg_med(iList))