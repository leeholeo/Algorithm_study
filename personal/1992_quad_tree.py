def quad_tree(lst, n):
    if n == 1:
        return lst[0]
    n2 = n//2
    lst1 = lst[:n2]
    lst2 = lst[n2:]
    lst1_l = [lst1[i][:n2] for i in range(n2)]
    lst1_r = [lst1[i][n2:] for i in range(n2)]
    lst2_l = [lst2[i][:n2] for i in range(n2)]
    lst2_r = [lst2[i][n2:] for i in range(n2)]
    result1_l = quad_tree(lst1_l, n2)
    result1_r = quad_tree(lst1_r, n2)
    result2_l = quad_tree(lst2_l, n2)
    result2_r = quad_tree(lst2_r, n2)
    if len(result1_l) == 1 and result1_l == result1_r == result2_l == result2_r:
        return result1_l
    else:
        return '(' + result1_l + result1_r + result2_l + result2_r + ')'


N = int(input())
video = [input() for _ in range(N)]
print(quad_tree(video, N))
