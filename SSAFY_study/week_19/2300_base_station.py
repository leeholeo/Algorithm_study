'''
dp
시간이 될 것도 같고 아닐 것도 같고
'''
def building_input(inp):
    x, y = map(int, inp.split())
    y = abs(y)
    x, y = map(lambda k: 2*k, (x, y))
    if building_y.get(x):
        building_y[x] = max(building_y[x], y)
    else:
        building_y[x] = y
        building_x.append(x)


import sys
input = sys.stdin.readline
LIMIT = 4000001
N = int(input())
building_y = {}
building_x = []
for _ in range(N):
    building_input(input())
building_x.sort()
length = len(building_x)
building_x.append(LIMIT)
building_y[LIMIT] = LIMIT
dp = [0] * length
dp[-1] = 1
for index in range(length):
    if dp[index-1] == 0:
        continue
    x = building_x[index]
    y = building_y[x]
    for i in range(index, length):
        ni = i + 1
        nx = building_x[ni]
        ny = building_y[nx]
        x_diff = nx - x
        if 2*y >= x_diff:
            if ny > y:
                # expand
                y = ny
            else:
                # next
                continue
        else:
            if dp[i] <= 1:
                dp[i] = dp[index-1] + y
            else:
                dp[i] = min(dp[i], dp[index-1] + y)
            y = max(ny, x_diff//2)
print(dp[-1]-1)
