'''
heap
'''
import sys
import heapq


input = sys.stdin.readline
N = int(input())
lecture = [tuple(map(int, input().split())) for _ in range(N)]
lecture.sort()
answer = 0
end = []
for s, e in lecture:
    heapq.heappush(end, e)
    if end[0] <= s:
        answer = max(answer, len(end)-1)
    while end[0] <= s:
        heapq.heappop(end)
answer = max(answer, len(end))
print(answer)