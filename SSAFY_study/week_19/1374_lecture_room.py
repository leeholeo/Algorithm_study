'''
누적 합
'''
from collections import defaultdict
import sys


input = sys.stdin.readline
N = int(input())
time_table = defaultdict(int)
time_list = set()
for _ in range(N):
    num, start, end = map(int, input().split())
    time_table[start] += 1
    time_table[end] -= 1
    time_list.add(start)
    time_list.add(end)
time_list = sorted(list(time_list))
max_overlap = 0
overlap = 0
for time in time_list:
    overlap += time_table[time]
    max_overlap = max(max_overlap, overlap)
print(max_overlap)
