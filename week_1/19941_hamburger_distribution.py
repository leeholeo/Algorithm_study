# 배치를 순회하면서 사람인 경우 선택할 수 있는 햄버거 중 가장 왼쪽에 있는 햄버거를 선택한다.
N, K = map(int, input().split())
table = input().strip()
ham_idx = -1
cnt = 0
for per_idx in range(N):
    if table[per_idx] == 'H':
        continue

    ham_idx = max(ham_idx, per_idx-K-1)
    try:
        while ham_idx < per_idx + K:
            ham_idx += 1
            if table[ham_idx] == 'H':
                cnt += 1
                break
    except IndexError:
        break

print(cnt)
