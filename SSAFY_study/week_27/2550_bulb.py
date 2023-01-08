'''
LIS
1. 몇 번째 위치인지 기록
2. 이전 index 기록
    2-1. 로그 전부 기록
'''
N = int(input())
top = list(map(int, input().split()))
bottom = list(map(int, input().split()))
bottom_to_top = []
converter = {}
for i in range(N):
    t = top[i]
    converter[t] = i
for i in range(N):
    b = bottom[i]
    top_index = converter[b]
    bottom_to_top.append(top_index)

LIS = [[(-1, 0)]]
line = 1
last = 0
for bulb_index, bulb in enumerate(bottom_to_top):
    insert_index = -1
    for i in range(len(LIS)-1, -1, -1):
        if bulb > LIS[i][-1][0]:
            insert_index = i + 1
            break
    if insert_index != last + 1:
        line += 1
    last = insert_index
    if insert_index == len(LIS):
        LIS.append([(bulb, line, bulb_index)])
    else:
        line += 1
        LIS[insert_index].append((bulb, line, bulb_index))

print(len(LIS) - 1)
answer = []
for i in range(len(LIS) - 1, 0, -1):
    for j in range(len(LIS[i]) - 1, -1, -1):
        if LIS[i][j][1] <= line:
            line = LIS[i][j][1]
            answer.append(bottom[LIS[i][j][2]])
            break
print(*sorted(answer), sep=' ')
