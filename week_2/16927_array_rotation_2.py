def rotation(row, col, r):
    half = min(row, col) // 2
    for k in range(half):
        # temp = left + down + right + up (CCW)
        temp_left = []
        temp_down = arr[row-1-k][k:col-k]
        temp_right = []
        temp_up = arr[k][k:col-k]
        temp_up.reverse()
        for i in range(k+1, row-k-1):
            temp_left.append(arr[i][k])
            temp_right.append(arr[row-1-i][col-1-k])

        # rotation
        temp = temp_left + temp_down + temp_right + temp_up
        len_temp = len(temp)
        go = r % len_temp
        temp = temp[-go:] + temp[:len_temp-go]
        # temp to arr
        len_temps = [len(temp_left), len(temp_down), len(temp_right), len(temp_up)]
        for i in range(2, -1, -1):
            for j in range(i+1, 4):
                len_temps[j] += len_temps[i]

        temp_left = temp[:len_temps[0]]
        temp_down = temp[len_temps[0]:len_temps[1]]
        temp_right = temp[len_temps[1]:len_temps[2]]
        temp_up = temp[len_temps[2]:len_temps[3]]
        arr[row-1-k][k:col-k] = temp_down
        temp_up.reverse()
        arr[k][k:col-k] = temp_up
        for i in range(k+1, row-k-1):
            try:
                arr[i][k] = temp_left.pop(0)
                arr[row-1-i][col-1-k] = temp_right.pop(0)
            except IndexError:
                pass


N, M, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
rotation(N, M, R)
for sub_arr in arr:
    print(*sub_arr)
