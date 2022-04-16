# # Brute force, 시간 초과
# n, k = map(int, input().split())
# coins = set()
# for _ in range(n):
#     coin = int(input())
#     if coin > k:
#         continue
#
#     coins.add(coin)
#
# coins = list(coins)
# coins.sort(reverse=True)
# result = 9876543210
# length = len(coins) - 1
#
#
# def brute(now=0, remain=k, accum=0):
#     global result
#     if accum >= result:
#         return
#
#     unit = coins[now]
#     share, remainder = divmod(remain, unit)
#     if remainder == 0:
#         result = min(result, share + accum)
#         return
#
#     if now == length:
#         return
#
#     for num in range(share, -1, -1):
#         brute(now+1, remain-num*unit, accum+num)
#
#
# brute()
# if result == 9876543210:
#     print(-1)
# else:
#     print(result)


# # DP
# n, k = map(int, input().split())
# coins = set()
# for _ in range(n):
#     coin = int(input())
#     if coin > k:
#         continue
#
#     coins.add(coin)
#
# coins = list(coins)
# coins.sort()
# length = len(coins)
# dp = [None] * (k+1)
# for i in range(len(coins)-1, -1, -1):
#     for j in range(1, k // coins[i] + 1):
#         if dp[coins[i] * j]:
#             continue
#
#         dp[coins[i] * j] = j
#
# for i in range(coins[0]+1, k+1):
#
#     mini = 9876543210
#     for j in range(coins[0], i-coins[0]):
#         try:
#             mini = min(mini, dp[j] + dp[i-j])
#         except TypeError:
#             continue
#     if dp[i]:
#         dp[i] = min(dp[i], mini)
#     else:
#         dp[i] = mini
#
# print(dp[k])


# dp (2)
# if result == 9876543210:
#     print(-1)
# else:
#     print(result)


# # DP (2)
n, k = map(int, input().split())
coins = set()
for _ in range(n):
    coin = int(input())
    if coin > k:
        continue

    coins.add(coin)

coins = list(coins)
coins.sort(reverse=True)
queue = [0]
visited = [0] * (k+1)
dp = [0] * (k+1)
now = 0


def coins_dp():
    while queue:
        now = queue.pop(0)
        for c in coins:
            nxt = now + c

            if nxt >= k:
                if nxt == k:
                    return dp[now] + 1
                else:
                    continue

            if visited[nxt]:
                continue

            visited[nxt] = 1
            dp[nxt] = dp[now] + 1
            queue.append(nxt)
    else:
        return -1


print(coins_dp())
