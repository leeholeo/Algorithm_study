def dfs_downhill(start, end, data):
    now = start[:]
    stack = []
    stack.append(start)
    visited = [[[] for _ in range(len(data[0]))] for _ in range(len(data))]
    direction = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    cnt = 0
    while True:
        for d in direction:
            temp = []
            if 0 <= now[0] + d[0] < len(data) and 0 <= now[1] + d[1] < len(data[0]):
                if data[now[0]][now[1]] > data[now[0] + d[0]][now[1] + d[1]]:
                    temp.append(d)

        if temp:
            stack.append(temp)
            for dir in temp:
                if not dir in visited[now[0], now[1]]:
                    visited[now[0], now[1]].append(dir)
                    now[0] += dir[0]
                    now[1] += dir[1]

        else:
            pop

        # 가능한 downhill을 전체 arr에 대해 계산해놓는 방법.



    return cnt

M, N = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(M)]
start = [0, 0]
end = [M - 1, N - 1]

print(dfs_downhill(start, end, data))