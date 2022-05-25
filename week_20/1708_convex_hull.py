import sys


def CCW(v1, v2, v3):
    (x1, y1), (x2, y2), (x3, y3) = v1, v2, v3
    return x1*y2 + x2*y3 + x3*y1 - y1*x2 - y2*x3 - y3*x1


def delete_grad(ver_tuple):
    ver_grad, ver_x, ver_y = ver_tuple
    return ver_x, ver_y


def distance(a, b):
    return abs(a[0]-b[0]) ** 2 + abs(a[1]-b[1]) ** 2


def larger_distance(a, b, c):
    return b if distance(a, b) > distance(a, c) else c


N = int(sys.stdin.readline())
vertexes = []
# y좌표가 최소인 정점을 찾는다. 여러 개라면 x좌표가 최대인 정점을 선택한다.
max_x, min_y = -40001, 40001
for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    if y > min_y:
        vertexes.append((x, y))
    elif y == min_y:
        if x > max_x:
            vertexes.append((max_x, min_y))
            max_x = x
        else:
            vertexes.append((x, y))
    else:
        vertexes.append((max_x, min_y))
        max_x = x
        min_y = y

# 각도에 따라 정렬한다. 시작점으로부터 기울기로 판단한다.
# 기울기의 경우에는 0~inf -inf~0 순으로 변하므로 양수와 음수를 나눠서 정렬한다.
gradient_vers_pos = []
gradient_vers_neg = []
gradient_vers_inf = []
for i in range(1, N):
    x, y = vertexes[i]
    dx = x - max_x
    dy = y - min_y
    if dx == 0:
        gradient_vers_inf.append((None, x, y))
        continue
    gradient = dy / dx
    if gradient > 0:
        gradient_vers_pos.append((gradient, x, y))
    else:
        gradient_vers_neg.append((gradient, x, y))
gradient_vers_pos.sort(reverse=True)
gradient_vers_neg.sort(reverse=True)
gradient_vers = [(None, max_x, min_y)] + gradient_vers_neg + gradient_vers_inf + gradient_vers_pos

# Graham scan
stack = [(max_x, min_y), delete_grad(gradient_vers.pop())]
while gradient_vers:
    first = stack[-2]
    second = stack[-1]
    next_ver = delete_grad(gradient_vers[-1])
    CCW_value = CCW(first, second, next_ver)
    if CCW_value > 0:
        gradient_vers.pop()
        stack.append(next_ver)
    elif CCW_value == 0:
        gradient_vers.pop()
        stack[-1] = larger_distance(first, second, next_ver)
    else:
        stack.pop()

print(len(stack)-1)
