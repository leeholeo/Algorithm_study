# # dfs
#
# import sys
#
#
# def dfs(now, checked):
#     if now >= N:
#         global result
#         result += 1
#         return
#
#     if 1 & now:
#         dfs(now+1, True)
#         dfs(now+1, False)
#     else:
#         dfs(now+3, True)
#         if checked:
#             dfs(now+2, False)
#         else:
#             dfs(now+1, False)
#
#
# sys.setrecursionlimit(2 * 10 ** 5)
# N = int(input())
# N *= 2
# result = 0
# dfs(0, False)
# print(result % 9901)
#

# dp
N = int(input())
a, b = 1, 1
c = b
for _ in range(N):
    c += a
    a += b << 1
    a %= 9901
    b = c

print(a)
