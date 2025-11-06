iter = int(input())

inputList = [list(map(int, input().split())) for _ in range(iter)]

sortList = sorted(inputList, key=lambda x: (x[0], -x[1]))

present = 1
total = 0

for i in range(iter):
    if sortList[i][0] == present:
        total += sortList[i][1]
        present += 1
    elif sortList[i][0] > present:
        present = sortList[i][0]
        total += sortList[i][1]
        present += 1
    else:
        continue

print(total)