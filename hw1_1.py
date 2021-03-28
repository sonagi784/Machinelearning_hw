result = 0
iList = ['cabc', 'xyza', 'abbc', '13221', 'xyzk']

for string in iList:
    if string[0] != string[-1]:
        result += 1

print(result)