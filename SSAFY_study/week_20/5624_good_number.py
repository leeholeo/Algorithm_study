'''
양방향 접근
'''
from collections import defaultdict
import sys
input = sys.stdin.readline
N = int(input())
pool = defaultdict(bool)
seq = list(map(int, input().split()))
good_cnt = 0
for i in range(N):
    for j in range(i):
        if pool[seq[i]-seq[j]]:
            good_cnt += 1
            break
    for j in range(i+1):
        pool[seq[i]+seq[j]] = True
print(good_cnt)
