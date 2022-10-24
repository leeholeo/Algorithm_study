"""
배열을 순회하며 첫 번째로 조건을 만족하는 idx 범위를 찾고(ex. 4:10 ...) 조건을 만족하도록 범위를 옮겨가며 찾기
"""
N, K = map(int, input().split())
dolls = list(map(int, input().split()))
ans = N + 1
ryan = 0
length = 0
back = 0
for forward in range(N):
    length += 1
    if dolls[forward] == 1:
        ryan += 1
    while ryan == K:
        if dolls[back] == 1:
            ryan -= 1
            ans = min(ans, length)
        length -= 1
        back += 1

if ans == N + 1:
    ans = -1
print(ans)
