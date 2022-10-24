'''
dp
'''
def price_to_int(price):
    return int(price.replace('.', ''))


def data_to_int(c, p):
    return int(c), price_to_int(p)


import sys
input = sys.stdin.readline
while True:
    n, m = data_to_int(*input().split())
    if n == m == 0:
        break
    m += 1
    dp = [0] * m
    dp[0] = 1
    candy = [data_to_int(*input().split()) for _ in range(n)]
    for i in range(m):
        if dp[i] == 0:
            continue
        for c, p in candy:
            if i+p >= m:
                continue
            dp[i+p] = max(dp[i+p], c+dp[i])
    print(max(dp)-1)
