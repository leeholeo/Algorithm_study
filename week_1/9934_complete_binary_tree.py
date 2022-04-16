K = int(input())
inorder = list(map(int, input().split()))
depths = [[] for _ in range(K+1)]


def depth_check(left, right, depth=1):
    if left == right:
        return
    half = (right - left) // 2
    depth_check(left, left+half, depth+1)
    depths[depth].append(str(inorder[left+half]))
    depth_check(right - half, right, depth+1)


depth_check(0, len(inorder))

for nodes in depths[1:]:
    print(' '.join(nodes))
