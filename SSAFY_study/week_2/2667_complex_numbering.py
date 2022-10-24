'''
사방탐색, dfs, 재귀, 개수는 리턴을 통해 전달
'''
directions = ((1, 0), (0, 1), (-1, 0), (0, -1))


def dfs(r, c):
    complex[r][c] = 0
    rtn = 1
    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if not (0 <= nr < N and 0 <= nc < N):
            continue
        if complex[nr][nc] == '1':
            rtn += dfs(nr, nc)
    return rtn


N = int(input())
complex = [' '.join(input()).split() for _ in range(N)]
numbers = []
for row in range(N):
    for col in range(N):
        if complex[row][col] == '1':
            numbers.append(dfs(row, col))
numbers.sort()
print(len(numbers))
print(*numbers, sep='\n')
