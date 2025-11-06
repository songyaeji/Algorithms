iter = int(input())

inputList = [list(map(int, input().split())) for _ in range(iter)]

sortList = sorted(inputList, key=lambda x: (x[0], -x[1]))

present = 1
noodle = 0
total = 0

for i in range(iter):
    if sortList[i][0] == present:
        if noodle < sortList[i][1]:
            noodle = sortList[i][1]
        else:
            continue
    else:
        present = sortList[i][0]
        total += noodle
        noodle = sortList[i][1]

total += noodle

print(total)
