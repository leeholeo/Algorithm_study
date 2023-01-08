'''
greedy
'''
from collections import defaultdict


N = int(input())
H = map(int, input().split())
arrows = defaultdict(int)
cnt = 0
for height in H:
    if arrows[height] == 0:
        cnt += 1
        arrows[height-1] += 1
    else:
        arrows[height] -= 1
        arrows[height-1] += 1
print(cnt)
