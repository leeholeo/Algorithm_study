# # 왜 실패햇지...
n, w, L = map(int, input().split())
trucks = list(map(int, input().split()))
time = 0
weight = 0
q = []
for t in trucks:
    while weight + t > L or len(q) >= w:
        front_time, front_weight = q.pop(0)
        time = front_time
        weight -= front_weight

    q.append((time + w, t))
    weight += t
    time += 1

print(q[-1][0] + 1)

# n, w, L = map(int, input().split())
# trucks = list(map(int, input().split()))
# time = 0
# weight = 0
# bridge = [0] * w
# while trucks:
#     time += 1
#     weight -= bridge.pop(0)
#
#     if weight + trucks[0] <= L:
#         t = trucks.pop(0)
#         bridge += [t]
#         weight += t
#     else:
#         bridge += [0]
#
# print(time + w)
