# border식이 더 빠른듯. 코드는 백준 제출에 있음.
import sys
R, C = map(int, sys.stdin.readline().split())
data = [sys.stdin.readline().rstrip() for _ in range(R)]
now = [0, 0]
# ASCII or dictionary
# visited = {'0': 1  # time over
visited = [0] * 256
visited[ord(data[now[0]][now[1]])] = 1
direction = [[1, 0], [0, 1], [-1, 0], [0, -1]]
stack = [0] * 27
top = 0
checked = -1
cnt = 1
max_cnt = 1
while True:
    for drc in range(checked + 1, 4):
        temp = [now[0] + direction[drc][0], now[1] + direction[drc][1]]

        if temp[0] < 0 or temp[0] >= R or temp[1] < 0 or temp[1] >= C:
            continue
        char_idx = ord(data[temp[0]][temp[1]])

        if visited[char_idx]:
            continue
        else:
            stack[top] = [now[0], now[1], drc]
            top += 1
            now = temp
            visited[char_idx] = 1
            checked = -1
            cnt += 1
            break
    else:
        try:
            visited[ord(data[now[0]][now[1]])] = 0
            top -= 1
            now[0], now[1], checked = stack[top]
            if cnt > max_cnt:
                max_cnt = cnt
            cnt -= 1
        except TypeError:
            break

print(max_cnt)


# # 최세진 교수님 코드(시간 초과)
# import sys
#
#
# r, c = map(int, sys.stdin.readline().split())
#
# MAP = [ sys.stdin.readline().rstrip() for _ in range(r) ]
#
# path = []
# # DAT <- Direct Access Table
# check = [0] * 256
# # check[index] -> index: 아스키코드값, value : 해당 아스키코드를 들린적 있는가?
# ans = 0
# def dfs(row, col, cnt):
#     global ans
#     ans = max(ans, cnt)
#     dr = [-1,1,0,0]
#     dc = [0,0,-1,1]
#     for i in range(4):
#         next_row = row + dr[i]
#         next_col = col + dc[i]
#         if 0 <= next_row < r and 0 <= next_col < c:
#             # 맵 안에 있어야 한다.
#             asc = ord(MAP[next_row][next_col]) # 아스키코드값 추출
#             if check[asc] == 1:
#                 continue
#                 # 이번에 들릴 문자는 기록하기도 전에 기록이 되어 있다.
#                 # 이미 들린 문자다.
#             check[asc] = 1 # 이 아스키코드값은 들렸다.
#             dfs(next_row, next_col, cnt + 1)
#             check[asc] = 0 # 갔다가 돌아와서는 기록 삭제
#
# check[ ord(MAP[0][0]) ] = 1
# dfs(0, 0, 1)
# print(ans)
