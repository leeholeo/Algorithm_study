from itertools import combinations


def cal_diff(idx):
    start = combies[idx]
    link = combies[-idx-1]
    s_stat = 0
    for s in start:
        for ss in start:
            s_stat += stats[s][ss]
    l_stat = 0
    for l in link:
        for ll in link:
            l_stat += stats[l][ll]
    return abs(s_stat - l_stat)


N = int(input())
stats = [list(map(int, input().split())) for _ in range(N)]
combies = list(combinations(range(N), N // 2))
mini = 9876543210
for i in range(len(combies) // 2):
    mini = min(mini, cal_diff(i))
    if mini == 0:
        break

print(mini)
