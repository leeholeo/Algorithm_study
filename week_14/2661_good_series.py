def dfs(series, length):
    if length == N:
        print(*series, sep='')
        quit()

    length += 1
    half_length = length // 2
    series.append(0)
    for n in range(1, 4):
        if series[-2] == n:
            continue

        series[-1] = n
        for l in range(1, half_length + 1):
            if series[-l:] == series[-2 * l: -l]:
                break
        else:
            dfs(series[:], length)


N = int(input())
dfs([1], 1)
