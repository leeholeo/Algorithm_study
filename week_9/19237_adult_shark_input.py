import random


f = open('19237_adult_shark_input.txt', 'w')
TESTCASE = 100
for tc in range(TESTCASE):
    random.seed(random.randint(1, 10000))
    N = random.randint(2, 20)
    M = random.randint(2, N ** 2)
    k = random.randint(1, 1000)
    sharks = random.sample(range(N ** 2), M)
    grid = ['0'] * (N ** 2)
    shark_cnt = 1
    directions = ['1', '2', '3', '4']
    for s in sharks:
        grid[s] = str(shark_cnt)
        shark_cnt += 1
    f.write(f'{N} {M} {k}\n')
    for i in range(N):
        f.write(' '.join(grid[0 + i * N:N + i * N]) + '\n')
    f.write(' '.join(map(str, random.choices(range(1, 5), k=M))) + '\n')
    for _ in range(4 * M):
        random.shuffle(directions)
        f.write(' '.join(directions) + '\n')

f.close()
