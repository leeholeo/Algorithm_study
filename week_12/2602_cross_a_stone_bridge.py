line = input()
bridge = [input(), input()]
length = len(bridge[0])
dp = [[0] * length + [1] for _ in range(2)]
converter = {'R': 0, 'I': 1, 'N': 2, 'G': 3, 'S': 4}
RINGS_idxes = [[[] for __ in range(2)] for _ in range(5)] + [[[-1], [-1]]]    # [r, i, n, g, s]
for i in range(2):
    for j in range(length):
        c_idx = converter[bridge[i][j]]
        RINGS_idxes[c_idx][i].append(j)
        # elif bridge[i][j] == 'I':
        #     RINGS_idxes[1][i].append(j)
        # elif bridge[i][j] == 'N':
        #     RINGS_idxes[2][i].append(j)
        # elif bridge[i][j] == 'G':
        #     RINGS_idxes[3][i].append(j)
        # elif bridge[i][j] == 'S':
        #     RINGS_idxes[4][i].append(j)

last_c_idx = 5
for l in line:
    temp_nxt = []
    for i in range(2):
        last_length = len(RINGS_idxes[last_c_idx][not i])
        c_idx = converter[l]
        for c in RINGS_idxes[c_idx][i]:
            least_idx = 0
            nxt = 0
            while least_idx < last_length:
                least_c = RINGS_idxes[last_c_idx][not i][least_idx]
                if least_c < c:
                    nxt += dp[not i][least_c]
                    least_idx += 1
                else:
                    break

            temp_nxt.append(nxt)

    for i in range(2):
        for c in RINGS_idxes[c_idx][i]:
            dp[i][c] = temp_nxt.pop(0)
    last_c_idx = c_idx

total = 0
for i in range(2):
    for c in RINGS_idxes[c_idx][i]:
        total += dp[i][c]

print(total)
