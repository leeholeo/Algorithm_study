'''
greedy
'''
N = int(input())
solutions = sorted(list(map(int, input().split())))
left = 0
right = -1
answer = solutions[left] + solutions[right]
while solutions[left] < solutions[right]:
    now = solutions[left] + solutions[right]
    if abs(answer) > abs(now):
        answer = now
    if abs(solutions[left]) > abs(solutions[right]):
        left += 1
    else:
        right -= 1
print(answer)
