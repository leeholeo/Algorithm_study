'''
dp
scv의 갯수가 변수라는 점에 주목하여 다양한 상황에 사용할 수 있는 코드를 작성하는 데 집중하였다.
1. n중첩 dp를 만들고 접근하는 함수
2. 모집단이 pool이고 길이가 length인 순열을 만드는 함수(swap식)
3. list 사이의 차 함수(matlab like)
greedy로는 왜 안되는 지 몰?루겠다.
'''
from collections import deque


def make_dp(depth):
    if depth == 0:
        return -1
    dp = []
    for _ in range(61):
        dp.append(make_dp(depth-1))
    return dp


# nPr일 때, n*n!/r!의 시간복잡도, 데이터를 복사하기 때문에 메모리가 많이 소모됨
def permutation(pool, length, depth=0):
    if length == depth:
        return perms.append(pool[:length])
    for i in range(depth, len(pool)):
        pool[depth], pool[i] = pool[i], pool[depth]
        permutation(pool[:], length, depth+1)
        pool[depth], pool[i] = pool[i], pool[depth]


def list_subtraction(list_a, list_b):
    for i in range(min(len(list_a), len(list_b))):
        list_a[i] -= list_b[i] if list_b[i] < list_a[i] else list_a[i]
    return list_a


def find_value(nested_list, coordinate):
    rtn = nested_list
    for coord in coordinate:
        rtn = rtn[coord]
    return rtn


def fill_value(nested_list, coordinate, value):
    n_list = nested_list
    for i in range(len(coordinate)-1):
        n_list = n_list[coordinate[i]]
    n_list[coordinate[-1]] = value


def solve(dp, queue, perms):
    while queue:
        cnt, now_healths = queue.popleft()
        for perm in perms:
            next_healths = list_subtraction(now_healths[:], perm)
            if next_healths == [0] * N:
                return cnt + 1
            if find_value(dp, next_healths) != -1:
                continue
            fill_value(dp, next_healths, cnt + 1)
            queue.append((cnt + 1, next_healths))


N = int(input())
healths = list(map(int, input().split()))
dp = make_dp(N)
fill_value(dp, healths, 0)
queue = deque()
queue.append((0, healths))
damage_pool = [9, 3, 1]
damages = damage_pool[:N]
perms = []
permutation(damages, N)
print(solve(dp, queue, perms))
