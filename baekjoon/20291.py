import sys
read = sys.stdin.readline

n = int(read().strip())

fileDict = {}

for _ in range(n):
    filename = read().strip()
    if filename not in fileDict:
        fileDict[filename] = 1
    else:
        fileDict[filename] += 1

fileDict = dict(sorted(fileDict.keys(), key = lambda x: x[0]))

for i in range(len(fileDict)):
    print(fileDict.keys()[i], fileDict[i])