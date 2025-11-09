import sys
import heapq

input = sys.stdin.readline

n = int(input())
meetings = [tuple(map(int, input().split())) for _ in range(n)]
meetings.sort(key=lambda x: x[0])

min_heap = []

for start, end in meetings:
    if min_heap and min_heap[0] <= start:
        heapq.heappop(min_heap)
    heapq.heappush(min_heap, end)

print(len(min_heap))