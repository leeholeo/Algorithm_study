'''
brute force
'''
import sys
input = sys.stdin.readline


def case_to_num(case):
    case_num = []
    for i in range(N):
        if 1<<i & case:
            case_num.append(i+1)
    return case_num


LIMIT = 9876543210
N = int(input())
min_nutrient = list(map(int, input().split()))
ingredient = [list(map(int, input().split())) for _ in range(N)]
min_cost = LIMIT
min_case = -1
for case in range(1, 1<<N):
    cost = 0
    nutrient = [0] * 4
    for i in range(N):
        if 1<<i & case:
            cost += ingredient[i][-1]
            for j in range(4):
                nutrient[j] += ingredient[i][j]
    for j in range(4):
        if nutrient[j] < min_nutrient[j]:
            break
    else:
        if cost < min_cost:
            min_cost = cost
            min_case = case
        elif cost == min_cost:
            # ex) 1 3 4 vs 1 3 4 8
            min_case_num = case_to_num(min_case)
            case_num = case_to_num(case)
            if case_num < min_case_num:
                min_cost = cost
                min_case = case
if min_cost == LIMIT:
    print(-1)
else:
    print(min_cost)
    print(*case_to_num(min_case), sep=' ')
