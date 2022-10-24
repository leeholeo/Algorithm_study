'''
대애애애충 1M정도 될 것 같은데..
일단 무지성 완탐
'''
import sys


input = sys.stdin.readline
directions = ((1, 0), (0, 1), (-1, 0), (0, -1))
N, M = map(int, input().split())
grid = [' '.join(input()).split() for _ in range(N)]
# 십자가 저장
crosses = []
# 전체 순회
for r in range(1, N-1):
    for c in range(1, M-1):
        if grid[r][c] == '.':
            continue

        # index 초과 방지용 limit
        limit = min((r, c, N-r-1, M-c-1))
        s = 1   # 십자가 길이
        while s <= limit:
            flag = False
            # 사방 확인하며 .이면 종료
            for dr, dc in directions:
                nr, nc = r + s * dr, c + s * dc
                if grid[nr][nc] == '.':
                    flag = True
                    break
            if flag:
                break

            # 사방 방문 처리(-)
            for dr, dc in directions:
                nr, nc = r + s * dr, c + s * dc
                grid[nr][nc] = '-'
            # 십자가 길이 늘리기
            s += 1
        s -= 1
        # 십자가 불가능
        if s == 0:
            continue
        # 중앙 방문 처리
        grid[r][c] = '-'
        # 십자가 기록
        crosses.append((r+1, c+1, s))

# 방문 안 된 점 유무 확인
for r in range(N):
    for c in range(M):
        # 불가능
        if grid[r][c] == '*':
            print(-1)
            break
    else:
        continue
    break
else:
    # 가능
    print(len(crosses))
    for cross in crosses:
        print(*cross)
