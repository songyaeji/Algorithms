import sys
read = sys.stdin.readline

caseCount = int(read())

answer = []

for _ in range(caseCount):
    numberCount = int(read())
    numberList = [0 for _ in range(numberCount)]
    for i in range(numberCount):
        number = read().strip()
        numberList[i] = number
    numberList.sort()
    for j in range(numberCount-1):
        ending = len(numberList[j])
        for k in range(j+1, numberCount):
            if numberList[j] == numberList[k][:ending]:
                answer.append("NO")
                exit(0)
            else:
                answer.append("YES")
                exit(0)

print(*answer, sep='\n')