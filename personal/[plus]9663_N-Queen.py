# 첫 줄에 두는 친구는 좌우대칭 가능.

def dfs1(n, now=0):
    global cnt
    for i in range(n//2):
        change_used(n, now, i, 1)
        dfs(n, now + 1)
        change_used(n, now, i, 0)

    cnt *= 2

    if n % 2:
        change_used(n, now, n//2, 1)
        dfs(n, now + 1)


def dfs(n, now):
    global cnt
    if now == n:
        cnt += 1
        return

    for i in range(n):
        if used_col[i]:
            continue
        if used_diag_plus[now + i]:
            continue
        if used_diag_minus[n - now - 1 + i]:
            continue

        change_used(n, now, i, 1)
        dfs(n, now+1)
        change_used(n, now, i, 0)


def change_used(n, now, i, possibility):
    used_col[i] = possibility
    used_diag_plus[now+i] = possibility
    used_diag_minus[n-now-1+i] = possibility


N = int(input())
cnt = 0
used_col = [0] * N
used_diag_plus = [0] * (2 * N - 1)
used_diag_minus = [0] * (2 * N - 1)
dfs1(N)
print(cnt)
