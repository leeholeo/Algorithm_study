# not this
# def pay(friend_idx):
#     global cnt
#     global k
#     if cnt == 0:
#         global maximal_remainder
#         maximal_remainder = max(maximal_remainder, k)
#         return
#
#     if friend_idx >= N:
#         return
#
#     if not is_friends[friend_idx] and friends_fee[friend_idx] <= k:
#         k -= friends_fee[friend_idx]
#         is_friends[friend_idx] = True
#         cnt -= 1
#         now_friends = []
#         for f in edges[friend_idx]:
#             if is_friends[f]:
#                 continue
#             is_friends[f] = True
#             now_friends.append(f)
#             cnt -= 1
#
#         pay(friend_idx+1)
#
#         for f in now_friends:
#             is_friends[f] = False
#             cnt += 1
#         is_friends[friend_idx] = False
#         cnt += 1
#         k += friends_fee[friend_idx]
#
#     pay(friend_idx+1)
#
#
# N, M, k = map(int, input().split())
# friends_fee = list(map(int, input().split()))
# is_friends = [False] * N
# edges = [[] for _ in range(N)]
# cnt = N
# for _ in range(M):
#     v, w = map(int, input().split())
#     v -= 1
#     w -= 1
#     edges[v].append(w)
#     edges[w].append(v)
#
# maximal_remainder = -1
# pay(0)
# if maximal_remainder > -1:
#     print(k-maximal_remainder)
# else:
#     print('Oh no')

def find(a):
    while is_friends[a]:
        a = is_friends[a]
    return a


def union(a, b):
    parent_a = find(a)
    parent_b = find(b)
    if parent_a != parent_b:
        fee_a = friends_fee[parent_a]
        fee_b = friends_fee[parent_b]
        if fee_a < fee_b:
            friends_fee[parent_b] = 0
            is_friends[parent_b] = parent_a
        else:
            friends_fee[parent_a] = 0
            is_friends[parent_a] = parent_b


N, M, k = map(int, input().split())
friends_fee = list(map(int, input().split()))
is_friends = [False] * N
for _ in range(M):
    v, w = map(int, input().split())
    v -= 1
    w -= 1
    union(v, w)

result = sum(friends_fee)
if result <= k:
    print(result)
else:
    print('Oh no')
