'''
mathematics
'''
N = int(input())
tree = list(map(int, input().split()))
cnt = sum(tree)
if cnt % 3:
    print('NO')
else:
    cnt //= 3
    cnt_one = sum([tree[i] % 2 for i in range(N)])
    if cnt_one > cnt:
        print('NO')
    else:
        print('YES')
