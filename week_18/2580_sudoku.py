# import sys
#
#
# TOTAL = 45
#
#
# def fill_row():
#     for r in range(9):
#         if len(case_r[r]) == 1:
#             count = 0
#             for c in range(9):
#                 count += sudoku[r][c]
#
#             for c in case_r[r].keys():
#                 sudoku[r][c] = TOTAL - count
#                 del blanks[(r, c)]
#                 del case_c[c][r]
#                 del case_s[3*(r//3) + c//3][3*(r%3) + c%3]
#             case_r[r] = {}
#
#
# def fill_col():
#     for c in range(9):
#         if len(case_c[c]) == 1:
#             count = 0
#             for r in range(9):
#                 count += sudoku[r][c]
#
#             for r in case_c[c].keys():
#                 sudoku[r][c] = TOTAL - count
#                 del blanks[(r, c)]
#                 del case_r[r][c]
#                 del case_s[3*(r//3) + c//3][3*(r%3) + c%3]
#             case_c[c] = {}
#
#
# def fill_square():
#     for s in range(9):
#         if len(case_s[s]) == 1:
#             count = 0
#             for r, c in case_s[s].values():
#                 for sr in range(3*(r//3), 3*(r//3)+3):
#                     for sc in range(3*(c//3), 3*(c//3)+3):
#                         count += sudoku[sr][sc]
#
#                 sudoku[r][c] = TOTAL - count
#                 del blanks[(r, c)]
#                 del case_r[r][c]
#                 del case_c[c][r]
#             case_s[s] = {}
#
#
# input = sys.stdin.readline
# sudoku = list(list(map(int, input().split())) for _ in range(9))
# blanks = {}
# case_r = [{} for _ in range(9)]
# case_c = [{} for _ in range(9)]
# case_s = [{} for _ in range(9)]
# for row in range(9):
#     for col in range(9):
#         if sudoku[row][col] == 0:
#             blanks[(row, col)] = 1
#
# for br, bc in blanks:
#     case_r[br][bc] = 1
#     case_c[bc][br] = 1
#     case_s[3*(br//3) + bc//3][3*(br%3) + bc%3] = (br, bc)
#
# while blanks:
#     fill_row()
#     fill_col()
#     fill_square()
#
# for row in range(9):
#     for col in range(9):
#         print(sudoku[row][col], end=' ')
#     print()
import sys


# 초기 상태에서 해당 위치에 들어갈 수 있는 수 배열을 반환
def check(crow, ccol):
    temp_possible = [True] * 10
    possible = []

    # 가로, 세로, 네모 확인
    def check_row(row, col):
        for c in range(9):
            temp_possible[sudoku[row][c]] = False

    def check_col(row, col):
        for r in range(9):
            temp_possible[sudoku[r][col]] = False

    def check_box(row, col):
        lefttop_r = row // 3 * 3
        lefttop_c = col // 3 * 3
        for r in range(lefttop_r, lefttop_r + 3):
            for c in range(lefttop_c, lefttop_c + 3):
                temp_possible[sudoku[r][c]] = False

    check_row(crow, ccol)
    check_col(crow, ccol)
    check_box(crow, ccol)
    for poss_idx in range(1, 10):
        if temp_possible[poss_idx]:
            possible.append(poss_idx)

    return possible


# dfs를 진행하며 해당 좌표에 해당 값이 들어갈 수 있는지를 확인
def check_one(crow, ccol, num):
    # 가로, 세로, 네모 확인
    def check_row(row, col, n):
        for c in range(9):
            if sudoku[row][c] == n:
                return False
        return True

    def check_col(row, col, n):
        for r in range(9):
            if sudoku[r][col] == n:
                return False
        return True

    def check_box(row, col, n):
        lefttop_r = row // 3 * 3
        lefttop_c = col // 3 * 3
        for r in range(lefttop_r, lefttop_r + 3):
            for c in range(lefttop_c, lefttop_c + 3):
                if sudoku[r][c] == n:
                    return False
        return True

    if check_row(crow, ccol, num) and check_col(crow, ccol, num) and check_box(crow, ccol, num):
        return True
    else:
        return False


# 빈 좌표를 순회하며 dfs를 실행
def dfs(depth):
    # 하나를 찾으면 전부 종료
    if depth == length:
        return True
    now_r, now_c = possible_idx[depth]
    for possi in possible_value[depth]:
        if check_one(now_r, now_c, possi):
            sudoku[now_r][now_c] = possi
            if dfs(depth+1):
                return True
            sudoku[now_r][now_c] = 0
    return False


possible_idx = []
possible_value = []
sudoku = list(list(map(int, sys.stdin.readline().split())) for _ in range(9))
# 빈 좌표와 그 좌표에 들어갈 수 있는 값 채우기
for row in range(9):
    for col in range(9):
        if sudoku[row][col]:
            continue
        possible_idx.append((row, col))
        possible_value.append(check(row, col))

length = len(possible_value)
dfs(0)
for sudo in sudoku:
    print(*sudo)
