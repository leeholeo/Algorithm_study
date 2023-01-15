'''
누적 합
테크닉?
'''
import bisect


N, K = map(int, input().split())
numbers = list(map(int, input().split()))
numbers_left = [0] * (N+1)
hashed = {K: [-1]}
now = 0
for i in range(N):
    now += numbers[i]
    numbers[i] = now
    if hashed.get(now+K):
        hashed[now+K].append(i)
    else:
        hashed[now+K] = [i]
answer = 0
for i in range(N):
    if hashed.get(numbers[i]):
        answer += bisect.bisect_left(hashed[numbers[i]], i)

print(answer)
