import sys
import heapq

input = sys.stdin.readline

iter = int(input())
problems = [tuple(map(int, input().split())) for _ in range(iter)]
problems.sort(key=lambda x: x[0])

min_heap = []
for deadline, reward in problems:
    heapq.heappush(min_heap, reward)
    if len(min_heap) > deadline:
        heapq.heappop(min_heap)

print(sum(min_heap))