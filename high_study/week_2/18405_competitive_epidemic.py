from collections import deque


N, K = map(int, input().split())
viruses = [[] for _ in range(K+1)]
petris = [0] * N
for i in range(N):
    line = input().split()
    for j in range(N):
        if line[j] != '0':
            viruses[int(line[j])].append((i, j))

    petris[i] = line

S, X, Y = map(int, input().split())
directions = ((1, 0), (0, 1), (-1, 0), (0, -1))
q = deque()
for virus in viruses:
    q.extend(virus)

temp_q = deque()
while S > 0:
    while q:
        now = q.popleft()
        for drc in directions:
            nxt = (now[0]+drc[0], now[1]+drc[1])
            if nxt[0] < 0 or nxt[1] < 0 or nxt[0] >= N or nxt[1] >= N:
                continue

            if petris[nxt[0]][nxt[1]] != '0':
                continue

            petris[nxt[0]][nxt[1]] = petris[now[0]][now[1]]
            temp_q.append(nxt)

    q = temp_q
    temp_q = deque()
    S -= 1

print(int(petris[X-1][Y-1]))
