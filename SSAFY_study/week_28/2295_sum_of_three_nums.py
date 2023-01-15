'''
'''
N = int(input())
U = sorted([int(input()) for _ in range(N)])
plus = set()
for i in range(len(U)):
    for j in range(i, len(U)):
        plus.add(U[j] + U[i])
minus = set()
for i in range(len(U)):
    for j in range(i, len(U)):
        minus.add((U[j] - U[i], (j, i)))
plus = sorted(list(plus))
minus = sorted(list(minus))
p, m = -1, -1
while True:
    if plus[p] == minus[m][0]:
        break
    elif plus[p] < minus[m][0]:
        m -= 1
    else:
        p -= 1
print(U[minus[m][1][0]])
