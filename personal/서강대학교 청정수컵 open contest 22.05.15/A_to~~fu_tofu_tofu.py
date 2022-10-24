N, M, K = map(int, input().split())
result = (M+K-3)%N if (M+K-3)%N else N
print(result)
