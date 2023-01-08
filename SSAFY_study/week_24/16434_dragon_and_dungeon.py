'''
greedy
'''
import sys


input = sys.stdin.readline
N, atk = map(int, input().split())
dungeon = [tuple(map(int, input().split())) for _ in range(N)]
for t, a, h in dungeon:
    if t == 2:
        atk += a
hp = 1
max_hp = 1
for i in range(-1, -N-1, -1):
    t, a, h = dungeon[i]
    if t == 1:
        hit = h // atk - 1
        if h % atk:
            hit += 1
        hp += a * hit
        if hp > max_hp:
            max_hp = hp
    else:
        hp = max(hp-h, 1)
        atk -= a
print(max_hp)
