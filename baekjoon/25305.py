#num = 총 사람 수, cutline = 수상 가능한 사람 수
num, cutline = input().split()
num = int(num)
cutline = int(cutline)

inputList = list(map(int, input().split())).sort(reverse=True)

print(inputList[cutline-1])