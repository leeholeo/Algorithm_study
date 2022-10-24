'''
구간합
'''
import sys


input = sys.stdin.readline
a, b, d, N = map(int, input().split())
birth_accum = [0] * (d+1)
birth_accum[0] = 1
for i in range(1, N+1):
    i %= d+1
    now_birth = birth_accum[max(-1, (i-a)%(d+1))] - birth_accum[max(-1, (i-b)%(d+1))]
    birth_accum[i] = (birth_accum[(i-1)%(d+1)] + now_birth) % 1000
print((birth_accum[N%(d+1)]-birth_accum[(N-d)%(d+1)])%1000)
