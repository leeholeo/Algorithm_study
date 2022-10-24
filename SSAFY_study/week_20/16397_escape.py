'''
dp
'''
N, T, G = map(int, input().split())
LIMIT = 100000
dp = [False] * LIMIT
dp[N] = True
stack = [N]
cnt = 1
if N == G:
    print(0)
    quit()
while stack and cnt <= T:
    next_stack = []
    while stack:
        now = stack.pop()
        a = now + 1
        if a < LIMIT and dp[a] is False:
            if a == G:
                print(cnt)
                quit()
            dp[a] = True
            next_stack.append(a)
        if now == 0:
            continue
        b = 2 * now
        if b >= LIMIT:
            continue
        b = str(b)
        b = str(int(b[0])-1) + b[1:]
        b = int(b)
        if dp[b] is False:
            if b == G:
                print(cnt)
                quit()
            dp[b] = True
            next_stack.append(b)
    stack = next_stack
    cnt += 1
print('ANG')
