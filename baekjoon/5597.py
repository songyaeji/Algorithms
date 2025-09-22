inputList = [int(input()) for _ in range(28)]
numList = [0 for _ in range(31)]

for i in inputList:
    numList[i] = i

for j in range(1,31):
    if numList[j] == 0:
        print(j)