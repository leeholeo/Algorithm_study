'''
DP
인 줄 알고 별에 별 짓을 다 했지만 중간에 안 된 다는 것을 깨달아버렸다!
따흐흑
그래서 그냥 서치 했다
눈물이 난다
나는 바보다
'''
# NUMBER = 0
# ARRAY = 1
# NON_SWITCHED = 0
# SWITCHED = 1
# def lamp_and(sn, c, s):
#     return [dp[sn][c][ARRAY][r] & lamp[s][c+1][r] for r in range(N)]
#
#
# def dp_step_non_switched(switch_num, col):
#     non_switched = lamp_and(switch_num, col, NON_SWITCHED)
#     sum_non_switched = sum(non_switched)
#     if sum_non_switched > dp[switch_num][col+1][0]:
#         dp[switch_num][col+1] = (sum_non_switched, non_switched)
#
#
# def dp_step_switched(switch_num, col):
#     switched = lamp_and(switch_num, col, SWITCHED)
#     sum_switched = sum(switched)
#     if sum_switched > dp[switch_num][col+1][0]:
#         dp[switch_num+1][col+1] = (sum_switched, switched)
#
#
# N, M = map(int, input().split())
# lamp_non_switched = list(zip(*list(list(map(int, list(input()))) for _ in range(N))))
# lamp_switched = [[0 if lamp_non_switched[r][c] else 1 for c in range(N)] for r in range(M)]
# lamp = [lamp_non_switched, lamp_switched]
# K = int(input())
# is_odd = K % 2
# max_switch = max(M, K)
# dp = [[(0, None) for _ in range(M)] for __ in range(max_switch+2)]
# dp[0][-1] = (-1, [True] * N)
#
# for j in range(-1, M-1):
#     for k in range(max_switch):
#         if dp[k][j][NUMBER] == 0:
#             break
#         dp_step_non_switched(k, j)
#         dp_step_switched(k, j)
#     else:
#         dp_step_non_switched(max_switch, j)
#
# answer = 0
# for k in range(is_odd, max_switch+1, 2):
#     answer = max(answer, dp[k][-1][NUMBER])
#
# print(answer)

N, M = map(int, input().split())
lamp = [input() for _ in range(N)]
K = int(input())
line_count = {None: 0}
is_odd = K % 2
for line in lamp:
    if line_count.get(line):
        line_count[line] += 1
    else:
        if not ((zero_cnt := line.count('0')) % 2 == is_odd and K >= zero_cnt):
            continue
        line_count[line] = 1
print(max(line_count.values()))
