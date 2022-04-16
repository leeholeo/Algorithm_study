numbers_raw = [
    '###...#.###.###.#.#.###.###.###.###.###',
    '#.#...#...#...#.#.#.#...#.....#.#.#.#.#',
    '#.#...#.###.###.###.###.###...#.###.###',
    '#.#...#.#.....#...#...#.#.#...#.#.#...#',
    '###...#.###.###...#.###.###...#.###.###'
]
numbers = []
for n in range(10):
    number = []
    for i in range(5):
        number.append(numbers_raw[i][4 * n: 4 * n + 3])
    numbers.append(number)
impossibles = [[set() for _ in range(3)] for __ in range(5)]
for row in range(5):
    for col in range(3):
        for idx, number in enumerate(numbers):
            if number[row][col] == '.':
                impossibles[row][col].add(idx)

N = int(input())
nums_raw = [input() for _ in range(5)]
nums = []
for n in range(N):
    num = []
    for i in range(5):
        num.append(nums_raw[i][4 * n: 4 * n + 3])
    nums.append(num)
aver = 0
for num in nums:
    N -= 1
    avail = set(range(10))
    for row in range(5):
        for col in range(3):
            if num[row][col] == '#':
                avail -= impossibles[row][col]

    if avail == set():
        aver = -1
        break

    aver += 10 ** N * sum(avail) / len(avail)

print(aver)
