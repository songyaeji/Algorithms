count = int(input())

def r_(n):
    if n - int(n) >= 0.5:
        return int(n) + 1
    else:
        return int(n)

if count == 0:
    print(0)
else:
    inputList = [int(input()) for _ in range(count)]
    inputList.sort()
    cut = r_(count*0.15)
    levelList = inputList[cut:(count-cut)]
    average = r_(sum(levelList)/len(levelList))
    print(average)