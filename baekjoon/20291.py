import sys
read = sys.stdin.readline

n = int(read().strip())

fileDict = {}

# 20920.py logic 참고
for _ in range(n):
    filename = read().strip().split('.')[-1]
    if filename not in fileDict:
        fileDict[filename] = 1
    else:
        fileDict[filename] += 1

fileDict = dict(sorted(fileDict.items()))

for key, value in fileDict.items():
    print(key, value)