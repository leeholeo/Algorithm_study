N, M, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
rs = list(map(int, input().split()))

for r in rs:
    if r == 1:
        arr = arr[::-1]
    elif r == 2:
        arr = [ar[::-1] for ar in arr]
    elif r == 3:
        arr = list(zip(*arr))
        arr = [ar[::-1] for ar in arr]
    elif r == 4:
        arr = list(zip(*arr))
        arr = arr[::-1]
    elif r == 5:
        n = len(arr)
        m = len(arr[0])
        temp = arr[n // 2:] + arr[:n // 2]
        for i in range(n // 2):
            arr[i] = temp[i][:m // 2] + arr[i][:m // 2]
        for i in range(n // 2, n):
            arr[i] = arr[i][m // 2:] + temp[i][m // 2:]
    elif r == 6:
        n = len(arr)
        m = len(arr[0])
        temp = arr[n // 2:] + arr[:n // 2]
        for i in range(n // 2):
            arr[i] = arr[i][m // 2:] + temp[i][m // 2:]
        for i in range(n // 2, n):
            arr[i] = temp[i][:m // 2] + arr[i][:m // 2]

for ar in arr:
    print(*ar)
