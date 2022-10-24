'''
heap
'''
import heapq


N, M = map(int, input().split())
heap = list(map(lambda x: [int(x)] * 2, input().split()))
heapq.heapify(heap)
while M > 1:
    staff = heapq.heappop(heap)
    staff[0] += staff[1]
    heapq.heappush(heap, staff)
    M -= 1
print(heap[0][0])
