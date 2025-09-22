numList = [0 for _ in range(31)]

for count in range(28):
    count = int(input())
    numList.append(count)

for i in range(1,31):
    if numList[i] == 0:
        print(numList.index[i])