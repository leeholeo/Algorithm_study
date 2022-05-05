TESTCASE = int(input())
for tc in range(TESTCASE):
    n = int(input())
    last_ranking = list(map(int, input().split()))
    edges = [[False] * (n+1) for _ in range(n+1)]
    # 검색 및 삭제에 많은 시간 소요, 따라서 인접 행렬로 변경
    # for idx in range(n-1):
    #     for rear_idx in range(idx+1, n):
    #         edges[idx].append(rear_idx)
    #         priorities[rear_idx].append(idx)
    #
    # m = int(input())
    # for _ in range(m):
    #     change_a, change_b = map(int, input().split())
    #     if change_a in edges[change_b]:

    for idx in range(n-1):
        for rear_idx in range(idx+1, n):
            now = last_ranking[idx]
            rear = last_ranking[rear_idx]
            edges[now][rear] = True

    m = int(input())
    for _ in range(m):
        a, b = map(int, input().split())
        edges[a][b], edges[b][a] = edges[b][a], edges[a][b]

    # priority가 없는지(앞에 설 사람의 수가 0인지) 빠르게 체크하기 위한 priorities list
    priorities = [0] * (n+1)
    nexts = []
    for col in range(1, n+1):
        cnt = 0
        for row in range(1, n+1):
            if edges[row][col]:
                cnt += 1
        priorities[col] = cnt
        if cnt == 0:
            nexts.append(col)
    # 1번이 두 명 이상인 경우
    if len(nexts) >= 2:
        print('?')
        continue

    answer = []
    while len(nexts) == 1:
        now = nexts.pop()
        answer.append(now)
        for col in range(1, n+1):
            if edges[now][col] is False:
                continue
            edges[now][col] = False
            priorities[col] -= 1
            if priorities[col] == 0:
                nexts.append(col)

    if len(nexts) >= 2:
        print('?')
    elif len(answer) != n:
        print("IMPOSSIBLE")
    else:
        print(*answer)
