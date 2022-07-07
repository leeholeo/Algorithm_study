'''
처음 생각했던 풀이는 2차원 배열에서 영역을 표시할 때 왼쪽 모서리와 오른쪽 모서리에 변화를 기록하는 방식
하지만 이는 (r2-r1) * skill 의 시간복잡도를 가지므로 불가능했다.
따라서 (r2-r1)을 상수 수준으로 줄여야 했다.
이 아이디어를 생각하는 부분이 어려웠다.
'''
# 이호형
def solution(board, skill):
    N = len(board)
    M = len(board[0])
    changes = [[] for _ in range(N+1)]

    for skill_type, r1, c1, r2, c2, degree in skill:
        if skill_type == 1:
            degree *= -1
        changes[r1].append((c1, c2+1, degree))
        changes[r2+1].append((c1, c2+1, -degree))

    line_change = [0] * (M+1)
    answer = 0
    region_change = 0
    for i in range(N):
        for c1, c2, degree in changes[i]:
            line_change[c1] += degree
            line_change[c2] -= degree

        for j in range(M):
            region_change += line_change[j]
            if region_change + board[i][j] > 0:
                answer += 1
        region_change += line_change[-1]
    return answer

'''
# for test
board = [[5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5]]
skill = [[1, 0, 0, 3, 4, 4], [1, 2, 0, 2, 3, 2], [2, 1, 0, 3, 1, 2], [1, 0, 1, 3, 3, 1]]
solution(board, skill)
'''