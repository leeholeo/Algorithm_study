'''
n번째 이동시 가능한 모든 경우 찾기, 유사 dp
'''
SAFE = '1'
DANGER = '0'
N, k = map(int, input().split())
# index error 방지용 자료 추가(k)
lines = [input() + '1' * k for _ in range(2)]
visited = [[False] * (N+k) for _ in range(2)]
# now -> nxt
now = [(0, 0)]
# 움직임 횟수(위험 지역)
cnt = 0
while now:
    nxt = []
    for lr, idx in now:
        # 도착
        if idx >= N:
            print(1)
            quit()

        # 방문배열 체크
        if visited[lr][idx]:
            continue
        visited[lr][idx] = True

        # 앞으로 가기
        if lines[lr][idx+1] is SAFE and visited[lr][idx+1] is False:
            nxt.append((lr, idx+1))

        # 뒤로 가기(위험 지역 체크)
        if idx - 1 > cnt:
            if lines[lr][idx-1] is SAFE and visited[lr][idx-1] is False:
                nxt.append((lr, idx-1))

        # 건너로 가기
        lr = (lr+1) % 2
        if lines[lr][idx+k] is SAFE and visited[lr][idx+k] is False:
            nxt.append((lr, idx+k))
    now = nxt
    cnt += 1
print(0)
