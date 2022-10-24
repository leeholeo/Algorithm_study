N, Kim, Lim = map(int, input().split())
N = len(bin(N)) - 2
Kim -= 1
Lim -= 1
cnt = 1
while not ((1 << (N - cnt)) & (Kim ^ Lim)):
    cnt += 1
print(N - cnt + 1)


# N, Kim, Lim = map(int, input().split())
# N = len(bin(N)) - 2
# Kim -= 1
# Lim -= 1
# print(len(bin(Kim ^ Lim))-2)
