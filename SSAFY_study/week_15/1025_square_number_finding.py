'''
brute force
'''
def is_square(number):
    left = 0
    right = 32000
    while left <= right:
        center = (left+right)//2
        center_square = center ** 2
        if center_square > number:
            right = center - 1
        elif center_square < number:
            left = center + 1
        else:
            return True
    return False


directions = ((1, 1), (1, -1), (-1, 1), (-1, -1))
n, m = map(int, input().split())
table = [list(input()) for _ in range(n)]
max_raw = -1
for i in range(n):
    for j in range(m):
        for ur, uc in directions:
            for dr in range(n):
                for dc in range(m):
                    if dr == 0 and dc == 0:
                        continue
                    now = ''
                    nr = i
                    nc = j
                    dr = ur * dr
                    dc = uc * dc
                    while 0 <= nr < n and 0 <= nc < m:
                        now += table[nr][nc]
                        nr += dr
                        nc += dc
                    now = int(now)
                    if now <= max_raw:
                        continue
                    if is_square(now):
                        max_raw = now
                    now = ''
print(max_raw)
