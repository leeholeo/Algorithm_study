'''
n 이하의 높이의 AVL tree의 최소 노드 수를 알고 있다면,
min_node_cnt(N+1) = root_node(1) + min_node_cnt(N) + min_node_cnt(N-1)
'''
T = int(input())
min_node_cnt = [None, 1, 2]
while min_node_cnt[-1] <= 1000000000:
    min_node_cnt.append(1 + min_node_cnt[-1] + min_node_cnt[-2])

for tc in range(T):
    nodes = int(input())
    for depth in range(1, len(min_node_cnt)):
        if nodes < min_node_cnt[depth]:
            print(depth-1)
            break
