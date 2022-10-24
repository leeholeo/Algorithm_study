'''
항상 가능하다,
총 두 가지로 나눌 수 있는데,
1. 한 축이 짝수인 경우: 짝수인 쪽을 2개씩 나누어서 ㄷ형(풀이는 역 ㄷ)으로 반복 이동하면 된다.
2. 모두 홀수인 경우: 3의 경우만 찾으면 나머지는 2개씩 나누어서 1번을 따르면 된다.
    3의 경우에는 좌상단에서 시작한다 했을 때 우측으로 쭉 간 후, 좌측으로 돌아가면서 위아래로 반복 이동하면 된다.
'''
# reverse 값에 따라 출력 순서를 변경 가능
def print_pair(a, b, is_reverse):
    print(f"({b},{a})") if is_reverse else print(f"({a},{b})")


# 한 축 짝수 이동(row 기준), col 기준일 시 reverse로 출력 순서만 바꿔줌
def snake(m, n, is_reverse):
    row = 0
    if is_reverse:
        m, n = n, m
    while row < m:
        for col in range(n):
            print_pair(row, col, is_reverse)
        row += 1
        for col in range(n-1, -1, -1):
            print_pair(row, col, is_reverse)
        row += 1


# 3 * 홀수 이동
def saw(m, n):
    # 좌 상단 기준
    row = m - 3
    row_upper_limit = row
    # 우측 직선 이동
    for col in range(n):
        print_pair(row, col, False)
    # 지그재그 이동
    sign = 1
    while col >= 0:
        row += sign
        while row_upper_limit < row < m:
            print_pair(row, col, False)
            row += sign
        col -= 1
        sign *= -1


T = int(input())
for tc in range(T):
    print(1)
    m, n = map(int, input().split())
    # 한 축이 1인 경우 예외
    if m == 1:
        for col in range(n):
            print_pair(0, col, False)
    # row가 짝수
    elif m % 2 == 0:
        snake(m, n, False)
    # col이 짝수
    elif n % 2 == 0:
        snake(m, n, True)
    # 둘 다 홀수
    else:
        # 두개씩 역 ㄷ 형으로 이동
        snake(m-3, n, False)
        # 3개만 남긴 후 지그재그
        saw(m, n)
