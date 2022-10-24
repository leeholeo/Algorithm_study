def five_stones(data):
    type = '0'
    # row inspection
    for i in range(19):
        cnt = 0
        for j in range(19):
            if data[i][j] == '0':
                cnt = 0
                continue
            elif data[i][j] != type:
                type = data[i][j]
                cnt = 1
            else:
                cnt += 1

            if cnt == 5:
                if data[i][j+1] == type:
                    continue

                row = i + 1
                col = j - 3
                return type, row, col

    # column inspection
    for i in range(19):
        cnt = 0
        for j in range(19):
            if data[j][i] == '0':
                cnt = 0
                continue
            elif data[j][i] != type:
                type = data[j][i]
                cnt = 1
            else:
                cnt += 1

            if cnt == 5:
                if data[j+1][i] == type:
                    continue

                row = j - 3
                col = i + 1
                return type, row, col

    # right-down diagonal inspection
    for k in range(-14, 15):
        cnt = 0
        for i in range(max(-k, 0), min(19, 19 - k)):
            if data[i][i+k] == '0':
                cnt = 0
                continue
            elif data[i][i+k] != type:
                type = data[i][i+k]
                cnt = 1
            else:
                cnt += 1

            if cnt == 5:
                if data[i+1][i+1+k] == type:
                    continue

                row = i - 3
                col = i + k - 3
                return type, row, col

    # left-down diagonal inspection
    for k in range(4, 33):
        cnt = 0
        for i in range(max(k - 18, 0), min(19, k + 1)):
            if data[i][k-i] == '0':
                cnt = 0
                continue
            elif data[i][k-i] != type:
                type = data[i][k-i]
                cnt = 1
            else:
                cnt += 1

            if cnt == 5:
                if data[i+1][k-i-1] == type:
                    continue

                row = i + 1
                col = k - i + 1
                return type, row, col

    return 0


data = [input().split() + ['0'] for _ in range(19)]
data += [['0'] * 20]

result = five_stones(data)
if not result:
    print(0)
else:
    print(result[0])
    print(result[1], result[2])
