'''
1. heapq 내의 min, max 힙 기능 사용
'''
import sys
import heapq


def _heappush_max(heap, item):
    heap.append(item)
    heapq._siftdown_max(heap, 0, len(heap)-1)


input = sys.stdin.readline
LIMIT = 1000000
N = int(input())
min_heap = [LIMIT]
max_heap = [-LIMIT]
min_length = 0
max_length = 0
for _ in range(N):
    now = int(input())
    if max_length > min_length:
        if max_heap[0] > now:
            heapq.heappush(min_heap, heapq._heapreplace_max(max_heap, now))
            min_length += 1
        else:
            heapq.heappush(min_heap, now)
            min_length += 1
    else:
        if now > min_heap[0]:
            _heappush_max(max_heap, heapq.heapreplace(min_heap, now))
            max_length += 1
        else:
            _heappush_max(max_heap, now)
            max_length += 1
    print(max_heap[0])


'''
2. 대소관계 재정의 클래스 사용
http://daplus.net/python-%ED%8C%8C%EC%9D%B4%EC%8D%AC%EC%97%90%EC%84%9C-max-heap-%EA%B5%AC%ED%98%84%EC%97%90-%EB%AC%B4%EC%97%87%EC%9D%84-%EC%82%AC%EC%9A%A9%ED%95%A9%EB%8B%88%EA%B9%8C/#:~:text=pop%20from%20maxheap-,%EB%8B%B5%EB%B3%80,-%ED%95%B4%EA%B2%B0%EC%B1%85%EC%9D%80%20%EA%B0%92%EC%9D%84%20%ED%9E%99%EC%97%90
'''
# import sys
# import heapq
#
#
# class MaxHeapObj(object):
#   def __init__(self, val): self.val = val
#   def __lt__(self, other): return self.val > other.val
#   def __str__(self): return str(self.val)
#
#
# input = sys.stdin.readline
# LIMIT = 1000000
# N = int(input())
# min_heap = [LIMIT]
# max_heap = [MaxHeapObj(-LIMIT)]
# min_length = 0
# max_length = 0
# for _ in range(N):
#     now = int(input())
#     if max_length > min_length:
#         if max_heap[0].val > now:
#             heapq.heappush(min_heap, heapq.heapreplace(max_heap, MaxHeapObj(now)).val)
#             min_length += 1
#         else:
#             heapq.heappush(min_heap, now)
#             min_length += 1
#     else:
#         if now > min_heap[0]:
#             heapq.heappush(max_heap, MaxHeapObj(heapq.heapreplace(min_heap, now)))
#             max_length += 1
#         else:
#             heapq.heappush(max_heap, MaxHeapObj(now))
#             max_length += 1
#     print(max_heap[0])
