import sys


input = sys.stdin.readline
N = int(input())
expected_ratings = [int(input()) for _ in range(N)]
expected_ratings.sort()
dissatisfaction_degree = [abs((i + 1) - expected_ratings[i]) for i in range(N)]
print(sum(dissatisfaction_degree))

print(sum([abs((i + 1) - er) for i, er in enumerate(sorted([int(input()) for _ in range(int(input()))]))]))
