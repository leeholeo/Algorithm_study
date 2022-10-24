import sys


sys.stdin = open('C:/Users/family/Desktop/temp/output.txt')


for _ in range(10):
    W = int(sys.stdin.readline())
    wires = [0] * W
    junctions = [[0] * W for _ in range(W)]
    for i in range(W):
        wires[i] = tuple(map(int, sys.stdin.readline().split()))

    nums_junction = [0] * W
    max_junc = 0
    for i in range(W):
        l1, r1 = wires[i]
        for j in range(i+1, W):
            l2, r2 = wires[j]
            if (l1-l2) * (r1-r2) < 0:
                junctions[i][j] = 1
                junctions[j][i] = 1

        nums_junction[i] = sum(junctions[i])
        max_junc = max(max_junc, nums_junction[i])

    cnt = 0
    cnt_lst = []
    for num in range(max_junc, 0, -1):
        for i in range(W):
            if nums_junction[i] == num:
                for j in range(W):
                    if junctions[i][j]:
                        junctions[j][i] = 0
                        nums_junction[j] -= 1

                junctions[i] = [0] * W
                nums_junction[i] = 0
                cnt += 1
                cnt_lst.append(wires[i])

    print(cnt_lst)

    # W = int(sys.stdin.readline())
    # wires = []
    # for i in range(W):
    #     wires.append(list(map(int, sys.stdin.readline().split())))
    #
    # wires.sort()
    # memo = [0] * 501
    # memo_lst = [[] for _ in range(501)]
    # for l, r in wires:
    #     memo[r] = max(memo[:r]) + 1
    #
    # print(W - max(memo))
