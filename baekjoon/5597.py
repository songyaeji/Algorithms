numList = [0 for i in range(31)]

for count in range(28):
    numList.append(int(input()))

for i in range(1,31):
    if i == 0:
        print(numList.index[i])