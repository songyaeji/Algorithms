count = int(input())
inputList = [int(input()) for _ in range(count)]
inputList.sort()

cut = round(count*0.15)

levelList = inputList[cut:(count-cut)]

average = round(sum(levelList)/len(levelList))

print(average)