import sys
read = sys.stdin.readline

caseCount = int(read())
answer = []

for _ in range(caseCount):
    numberCount = int(read())
    numberList = [read().strip() for _ in range(numberCount)]
    numberList.sort()
    isConsistent = True
    for j in range(numberCount - 1):
        if numberList[j] == numberList[j+1][:len(numberList[j])]:
            answer.append("NO")
            isConsistent = False
            break
    if isConsistent:
        answer.append("YES")

print(*answer, sep='\n')