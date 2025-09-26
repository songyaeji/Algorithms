n = int(input())
nList = list(map(int, input().split()))
m = int(input())
mList = list(map(int, input().split()))

answer = []

for i in mList:
    if i in nList:
        answer.append(1)
    else:
        answer.append(0)

print(*answer)