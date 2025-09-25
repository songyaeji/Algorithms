# A는 재배열이 가능하나, B는 재배열 불가능
count = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

#A는 오름차순, b는 내림차순 정렬한 후 dictionary로 매칭(이때 key는 B, value는 A)
tempA = sorted(A)
tempB = sorted(B, reverse=True)

abMap = dict(zip(tempB, tempA))

for num in range(count):
    A[num] = abMap[B[num]]

answer = sum([i*j for i, j in zip(A, B)])

print(answer)