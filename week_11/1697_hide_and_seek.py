N, K = map(int, input().split())
if N >= K:
    print(N - K)
else:
    positions = [-1] * 2 * K
    positions[N] = 0
    stack = [N]
    cnt = 0
    while positions[K] == -1:
        temp_stack = []
        cnt += 1
        while stack:
            now = stack.pop()
            back = now - 1
            front = now + 1
            warp = now * 2
            if back >= 0 and positions[back] == -1:
                positions[back] = cnt
                temp_stack.append(back)
            if front <= 2 * K and positions[front] == -1:
                positions[front] = cnt
                temp_stack.append(front)
            if warp <= 2 * K and positions[warp] == -1:
                positions[warp] = cnt
                temp_stack.append(warp)

        stack = temp_stack

    print(cnt)


# # 안됨
# LARGE_NUM = 9876543210
# N, K = map(int, input().split())
# if N >= K:
#     print(N - K)
# else:
#     N_bin = str(bin(N))[2:]
#     K_bin = str(bin(K))[2:]
#     N_len = len(N_bin)
#     K_len = len(K_bin)
#     idx = 0
#     while idx < N_len:
#         n_b = N_bin[idx]
#         k_b = K_bin[idx]
#         if n_b != k_b:
#             break
#
#         idx += 1
#
#     N_diff = int(N_bin[idx:N_len], 2)
#     K_diff = int(K_bin[idx:N_len], 2)
#     diff = abs(N_diff - K_diff)
#     up = LARGE_NUM
#     down = LARGE_NUM
#     if idx == 1:
#         up = 2 ** N_len - N_diff + int(K_bin[idx:N_len + 1], 2)
#         down = N_diff + 1 + int('1' * (N_len - idx - 1), 2) - int(K_bin[idx:N_len - 1], 2)
#         up += K_bin.count('1', N_len + 1, K_len) + K_len - (N_len + 1)
#         down += K_bin.count('1', N_len - 1, K_len) + K_len - (N_len - 1)
#
#     diff += K_bin.count('1', N_len, K_len) + K_len - N_len
#
#     print(min(diff, up, down))