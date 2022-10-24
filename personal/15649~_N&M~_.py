N, M = map(int, input().split())
data = list(map(int, input().split()))
# data.sort()
# numset = [data[0]]
# left = [1]
# for i in range(1, len(data)):
#     if data[i-1] == data[i]:
#         left[-1] += 1
#     else:
#         numset.append(data[i])
#         left.append(1)
numset = sorted(list(set(data)))

ans = [0] * M


def permutation(n, m, k=0, l=0):
    if k == m:
        print(' '.join(map(str, ans)))
        return

    for num in range(l, n):
        # if left[num]:
            ans[k] = numset[num]
        #     left[num] -= 1
            permutation(n, m, k + 1, num)
            # left[num] += 1


permutation(len(numset), M)
