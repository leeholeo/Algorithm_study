import sys
sys.setrecursionlimit(10001)


pre_order = []
while 10001:
    try:
        temp = int(input())
        pre_order.append(temp)
    except EOFError:
        break


def post_order(s=0, e=len(pre_order)):
    if s >= e:
        return

    for i in range(s+1, e):
        if pre_order[i] > pre_order[s]:
            post_order(s+1, i)
            post_order(i, e)
            break
    else:
        post_order(s+1, e)

    print(pre_order[s])


post_order()
