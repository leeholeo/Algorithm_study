'''
greedy
고려할 게 생각보다 많았음, 완탐이 훨씬 편함
비슷한 로직, 깔끔한 코드: https://www.acmicpc.net/source/11818442
'''
def idx_to_front(front_idx, now_idx):
    if front_idx == now_idx:
        return A
    return A[:front_idx] + A[now_idx] + A[front_idx:now_idx] + A[now_idx+1:]


A, B = input().split()
len_A = len(A)
len_B = len(B)
A = ''.join(sorted(A, reverse=True))
if len_A > len_B:
    print(-1)
elif len_A < len_B:
    print(A)
else:
    B_idx = 0
    A_idx = 0
    while B_idx < len_A:
        if B[B_idx] < A[A_idx]:
            A_idx += 1
            if A_idx == len_A:
                if B_idx == 0:
                    A = '-1'
                    break
                B_idx -= 1
                while B[B_idx] == '0':
                    B_idx -= 1
                    if B_idx < 0:
                        A = '-1'
                        break
                A_idx = B_idx
                A = A[:A_idx] + ''.join(sorted(A[A_idx:], reverse=True))
                B = B[:B_idx] + str(int(B[B_idx]) - 1) + '9' * (len_B-B_idx-1)
        elif B[B_idx] > A[A_idx]:
            A = idx_to_front(B_idx, A_idx)
            break
        else:
            A = idx_to_front(B_idx, A_idx)
            B_idx += 1
            A_idx = B_idx
    if A[0] == '0':
        print(-1)
    else:
        print(A)
