import sys
read = sys.stdin.readline

n, standard = read().strip().split()
n = int(n)
standard = int(standard)

vocabDict = {}

for _ in range(n):
    word = read().strip()
    if len(word) >= standard:
        if word not in vocabDict:
            vocabDict[word] = 1
        else:
            vocabDict[word] += 1
    else:
        continue

vocabDict = dict(sorted(vocabDict.items(), key = lambda x: x[1], reverse=True))
vocabList = list(vocabDict.keys())

for i in range(len(vocabList)):
    if vocabDict[vocabList[i]] == vocabDict[vocabList[i+1]]:
        if len(vocabList[i]) < len(vocabList[i+1]):
            vocabList[i], vocabList[i+1] = vocabList[i+1], vocabList[i]
        else:
            continue
    else:
        continue

print(*vocabList, sep='\n')