def equ_interval(iList, num):
    interval = (iList[1] - iList[0]) // num
    
    retarr = []
    nextnum = iList[0]
    for i in range(num):
        retarr.append([nextnum, nextnum+interval])
        nextnum += interval
    
    return retarr