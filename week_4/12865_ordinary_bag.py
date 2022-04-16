# # ver 2: dp by dict
# N, K = map(int, input().split())
# stuffs = [(map(int, input().split())) for _ in range(N)]
# dp = {0: 0}
# for w, v in stuffs:
#     temp_dp = {}
#     for key, value in dp.items():
#         temp_dp[key + w] = value + v
#
#     for key, value in temp_dp.items():
#         if key > K:
#             continue
#
#         dp[key] = max(dp.get(key, 0), value)
#
# print(max(dp.values()))


# ver 3: dp by list
N, K = map(int, input().split())
stuffs = [tuple(map(int, input().split())) for _ in range(N)]
dp = [0] * (K+1)
dp[0] = 1
for w, v in stuffs:
    for i in range(K-w, -1, -1):
        de = 1
        if dp[i]:
            dp[i+w] = max(dp[i+w], dp[i]+v)

de = 1
print(max(dp)-1)



# # ver 1: dfs
# import sys
#
#
# input = sys.stdin.readline
# N, K = map(int, input().split())
# stuffs = []
# for _ in range(N):
#     W, V = map(int, input().split())
#     if W > K:
#         continue
#
#     stuffs.append((V, W))
#
# stuffs.sort(key=lambda x: x[0] // x[1], reverse=True)
# rv = [0]  # remainder_values
# for i in range(N-1, -1, -1):
#     rv = [rv[0]+stuffs[i][0]] + rv
#
# maxi = 0
#
#
# def dfs(now, value, weight):
#     global maxi
#
#     if weight >= K:
#         if weight == K:
#             maxi = max(maxi, value)
#
#         return
#
#     if now == N:
#         maxi = max(maxi, value)
#         return
#
#     if maxi > rv[now] + value:
#         return
#
#     dfs(now+1, value+stuffs[now][0], weight+stuffs[now][1])
#     dfs(now+1, value, weight)
#
#
# dfs(0, 0, 0)
# print(maxi)
