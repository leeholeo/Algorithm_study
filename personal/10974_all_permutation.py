N = int(input())
used = [0] * (N + 1)
result = [0] * N


def permutation(n, k=0):
    if k == n:
        print(' '.join(map(str, result)))
        return

    for num in range(1, n+1):
        if used[num]:
            continue
        used[num] = 1
        result[k] = num
        permutation(n, k+1)
        used[num] = 0


permutation(N)
