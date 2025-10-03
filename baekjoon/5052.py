import sys
read = sys.stdin.readline

caseCount = int(read())

for _ in range(caseCount):
    numberCount = int(read())
    numberList = [0 for _ in range(numberCount)]
    for i in range(numberCount):
        number = read().strip()
        numberList[i] = number
    numberList.sort()
    for j in range(len(numberList)-1):
        ending = len(numberList[j])
        if numberList[j] == numberList[j+1][:ending]:
            print("NO")
            break
        else:
            print("YES")
            break