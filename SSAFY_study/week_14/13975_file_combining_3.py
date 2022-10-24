'''
Greedy heap
'''
import sys
import heapq


input = sys.stdin.readline
T = int(input())
for testcase in range(T):
    K = int(input())
    files = list(map(int, input().split()))
    heapq.heapify(files)
    answer = 0
    for _ in range(K-1):
        new_file = heapq.heappop(files) + heapq.heappop(files)
        answer += new_file
        heapq.heappush(files, new_file)
    print(answer)
