import sys


def plus(a, b):
    smallest_a = check(a)
    smallest_b = check(b)
    if smallest_a > smallest_b:
        set_[smallest_b] = smallest_a
    else:
        set_[smallest_a] = smallest_b


def check(c):
    setc = set_[c]
    if setc == c:
        return c

    smallest = check(setc)
    set_[c] = smallest
    return smallest


N, M = map(int, sys.stdin.readline().split())
set_ = [i for i in range(N+1)]
for _ in range(M):
    question, A, B = map(int, sys.stdin.readline().split())
    if question:
        if check(A) == check(B):
            print('yes')
        else:
            print('no')
    else:
        plus(A, B)
