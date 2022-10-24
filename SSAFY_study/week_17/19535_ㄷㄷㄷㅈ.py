'''
트리의 특성: 사이클이 없다
%DUDUDUNGJANG-트리가 맞다고 생각합니다%
+) 굳이 전파고 뭐고 할 필요가 없었다.
그냥 숫자만 세고 가운데 간선 고정에 양쪽 끝 개수만 곱해주면 됐다...
'''
class Node:
    all_node = {}
    leaf = []
    du_cnt = 0
    jang_cnt = 0

    def __init__(self, num):
        self.num = num
        self.adjacent = {}
        self.propagation = [0] * 4
        self.propagation[0] = None
        Node.all_node[num] = self

    def prop_to(self, to):
        Node.du_cnt += self.propagation[2] + to.propagation[2] + self.propagation[1]*to.propagation[1]
        to.propagation[1] += 1
        to.propagation[2] += self.propagation[1]

    def leaf_check(self):
        if len(self.adjacent) <= 1:
            Node.leaf.append(self)

    def cut(self):
        if not Node.all_node.get(self.num):
            return
        for adj_node in self.adjacent.values():
            self.prop_to(adj_node)
            del(adj_node.adjacent[self.num])
            adj_node.leaf_check()
        del(Node.all_node[self.num])

    @staticmethod
    def leaf_check_all():
        for node in Node.all_node.values():
            node.leaf_check()

    @staticmethod
    def cut_all():
        while Node.leaf:
            leaf_node = Node.leaf.pop()
            leaf_node.cut()

    @staticmethod
    def cnt_du():
        Node.leaf_check_all()
        Node.cut_all()

    @staticmethod
    def cnt_jang():
        for node in Node.all_node.values():
            adj_cnt = len(node.adjacent)
            Node.jang_cnt += adj_cnt * (adj_cnt-1) * (adj_cnt-2) // 6

    @staticmethod
    def du_jang_check():
        Node.cnt_jang()
        Node.cnt_du()
        if Node.du_cnt > 3 * Node.jang_cnt:
            return 'D'
        elif Node.du_cnt < 3 * Node.jang_cnt:
            return 'G'
        else:
            return 'DUDUDUNGA'

    @staticmethod
    def link(node_a, node_b):
        node_a.adjacent[node_b.num] = node_b
        node_b.adjacent[node_a.num] = node_a

    @staticmethod
    def get(num):
        return Node.all_node[num]


import sys
input = sys.stdin.readline
N = int(input())
for i in range(N+1):
    Node(i)
for _ in range(N-1):
    a, b = map(int, input().split())
    Node.link(Node.get(a), Node.get(b))
print(Node.du_jang_check())
