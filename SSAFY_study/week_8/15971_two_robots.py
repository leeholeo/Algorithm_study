'''
특정 점으로부터 다른 점까지의 최소 거리, 그런데 그 중 한 간선을 0으로 하는 문제로 볼 수 있다.
따라서 dp와 유사한 방식으로 한 간선을 0으로 했는지를 기록하는 변형 dijkstra를 시도해 보자.
'''
import heapq
import sys


def dijkstra():
    NORMAL = 0
    ZEROED = 1
    distance = [[INF] * N for _ in range(2)]
    # start == end 인 테케 존재, 시작 위치 초기화 없으면 틀림
    distance[NORMAL][start] = 0
    distance[ZEROED][start] = 0
    # 힙 초기화
    heap = []
    for length, destination in edges[start]:
        heapq.heappush(heap, (length, NORMAL, destination))
        distance[NORMAL][destination] = length
        heapq.heappush(heap, (0, ZEROED, destination))
        distance[ZEROED][destination] = 0
    # dijkstra
    while heap:
        length, state, destination = heapq.heappop(heap)
        if length > distance[state][destination]:
            continue
        for next_length, next_destination in edges[destination]:
            total_length = length + next_length
            # 현재 간선 0처리
            if state == NORMAL and length < distance[ZEROED][next_destination]:
                distance[ZEROED][next_destination] = length
                heapq.heappush(heap, (length, ZEROED, next_destination))
            # 상태 그대로 유지하며 일반 dijkstra
            if total_length < distance[state][next_destination]:
                distance[state][next_destination] = total_length
                heapq.heappush(heap, (total_length, state, next_destination))
    return distance[ZEROED][end]


input = sys.stdin.readline
INF = 10 ** 9
N, start, end = map(int, input().split())
start -= 1
end -= 1
# 트리화
edges = [[] for _ in range(N)]
for i in range(N-1):
    a, b, l = map(int, input().split())
    a -= 1
    b -= 1
    edges[a].append((l, b))
    edges[b].append((l, a))
print(dijkstra())
