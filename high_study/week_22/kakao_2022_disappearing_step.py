'''
풀이 1. aloc == bloc
풀이 2. b[r][c] == 0
풀이 1과 2의 유의미한 차이는 있지만, 풀이 1의 경우 함수의 전달인자를 list 형태로 넘겨줘야 한다.
이는 aloc == bloc의 계산에서 좌표는 같으나 하나는 tuple, 하나는 list인 경우가 존재하기 때문이다.(a 첫 번째 이동 시 같은 좌표인 경우)
시간상 더 많은 경우에서 풀이 1이 근소하게 빠르긴 하나 경우마다 다르고, 1/100 수준이라 의미가 없다.
'''
def solution(board: [[]], aloc: [int, int], bloc: [int, int]):
    row = len(board)
    col = len(board[0])
    directions = ((1, 0), (0, 1), (-1, 0), (0, -1))

    # a 이동, bmove를 호출한다. bmove는 amove를 호출하며 재귀적으로 작동한다.
    def amove(aloc, bloc, depth: int) -> (str, int):
        r, c = aloc
        # # 1. a와 b의 좌표가 같다면
        # if aloc == bloc:
        #     # 사방탐색
        #     for dr, dc in directions:
        #         nr, nc = r + dr, c + dc
        #         if not (0 <= nr < row and 0 <= nc < col) or board[nr][nc] == 0:
        #             continue
        #         # 갈 곳이 있다면 a(본인) 승
        #         return 'a', depth + 1
        #     # 갈 곳이 없다면 b(상대) 승
        #     return 'b', depth
        # 2. 현재 좌표에 발판이 없다면 b(상대) 승
        if board[r][c] == 0:
            return 'b', depth

        # 재귀로 선택되는 경우들
        cases = []
        # 사방탐색
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if not (0 <= nr < row and 0 <= nc < col) or board[nr][nc] == 0:
                continue
            # 갈 곳이 있다면 dfs, backtracking
            board[r][c] = 0
            cases.append(bmove((nr, nc), bloc, depth+1))
            board[r][c] = 1
        # 모든 경우 중에서 이기는 경우
        min_dep = []
        # ~ 지는 경우
        max_dep = []
        for winner, dep in cases:
            if winner == 'a':
                min_dep.append(dep)
            else:
                max_dep.append(dep)
        # 이기는 경우가 있다면 최소 이동 선택
        if min_dep:
            win = ('a', min(min_dep))
        # 지는 경우만 있다면 최대 이동 선택
        elif max_dep:
            win = ('b', max(max_dep))
        # 갈 수 있는 경우가 없다면 종료
        else:
            win = ('b', depth)

        return win

    def bmove(aloc, bloc, depth) -> (str, int):
        r, c = bloc
        # if aloc == bloc:
        #     for dr, dc in directions:
        #         nr, nc = r + dr, c + dc
        #         if not (0 <= nr < row and 0 <= nc < col) or board[nr][nc] == 0:
        #             continue
        #         return 'b', depth + 1
        #     return 'a', depth
        if board[r][c] == 0:
            return 'a', depth

        cases = []
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if not (0 <= nr < row and 0 <= nc < col) or board[nr][nc] == 0:
                continue
            board[r][c] = 0
            cases.append(amove(aloc, (nr, nc), depth+1))
            board[r][c] = 1
        min_dep = []
        max_dep = []
        for winner, dep in cases:
            if winner == 'b':
                min_dep.append(dep)
            else:
                max_dep.append(dep)
        if min_dep:
            win = ('b', min(min_dep))
        elif max_dep:
            win = ('a', max(max_dep))
        else:
            win = ('a', depth)

        return win

    return amove(aloc, bloc, 0)[1]
#
#
# board = [[1, 1, 1, 0], [1, 1, 0, 1], [1, 0, 1, 1], [0, 1, 1, 1]]
# aloc = [0, 0]
# bloc = [3, 3]
# print(solution(board, aloc, bloc))
