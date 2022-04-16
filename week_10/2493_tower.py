N = int(input())
towers = [987654321] + list(map(int, input().split()))
lasers = [0]
answers = [0] * (N + 1)
for i in range(N, 0, -1):
    while towers[i] >= towers[lasers[-1]]:
        answers[lasers.pop()] = i
    lasers.append(i)

answers.pop(0)
print(*answers)
