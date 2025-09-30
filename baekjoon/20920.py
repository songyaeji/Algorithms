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

vocabList = sorted(
    vocabDict.keys(),
    key=lambda x: (-vocabDict[x], -len(x), x)
)

print(*vocabList, sep='\n')