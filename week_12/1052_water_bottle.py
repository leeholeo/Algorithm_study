N, K = map(int, input().split())
N_str = bin(N)[2:]
length = len(N_str)
idx = 0
while idx < length:
    if K == 0:
        N_over = int(N_str[idx:], 2)
        if N_over:
            print(2 ** (length - idx) - N_over)
            break
        else:
            print(0)
            break
    if N_str[idx] == '1':
        K -= 1

    idx += 1
else:
    print(0)
