'''
Implementation
block[type][direction][0] = len(height diff list)
block[type][direction][1] = height diff list
'''
def is_block_fit() -> 1 or 0:
    j = i
    for k in range(length):
        j += 1
        if field[i] != field[j] - difference[k]:
            return 0
    return 1


block = [None,
         [[0, []], [3, [0, 0, 0]]],
         [[1, [0]]],
         [[1, [-1]], [2, [0, 1]]],
         [[1, [1]], [2, [-1, -1]]],
         [[1, [-1]], [1, [1]], [2, [0, 0]], [2, [-1, 0]]],
         [[1, [0]], [1, [-2]], [2, [0, 0]], [2, [1, 1]]],
         [[1, [0]], [1, [2]], [2, [0, 0]], [2, [0, -1]]]
         ]

C, P = map(int, input().split())
field = list(map(int, input().split()))
answer = 0
for i in range(C):
    for rotation in block[P]:
        length, difference = rotation
        if i + length >= C:
            continue
        answer += is_block_fit()
print(answer)
