# # ver 1
# rows, cols = map(int, input().split())
# cheeses = [input().split() for _ in range(rows)]
# directions = ((1, 0), (0, 1), (-1, 0), (0, -1))
# edges = []
# for drc in directions:
#     if drc[0] + drc[1] > 0:
#         i, j = 0, 0
#     else:
#         i, j = -1, -1
#
#     if drc[0]:
#         first, second = rows, cols
#     else:
#         first, second = cols, rows
#
#     before = '0'
#     for __ in range(second):
#         cnt = 0
#         for _ in range(first):
#             if cheeses[i][j] != before:
#                 if before == '0':
#                     cheeses[i][j] = 'c'
#                     edges.append((i, j))
#                 else:
#                     if cheeses[i - drc[0]][j - drc[1]] != 'c':
#                         cheeses[i - drc[0]][j - drc[1]] = 'c'
#                         edges.append((i - drc[0], j - drc[1]))
#
#             i += drc[0]
#             j += drc[1]


# # ver 2
# def melt():
#     for dx, dy in directions:
#         outer_iter = cols
#         inner_iter = rows
#         if dy:
#             outer_iter, inner_iter = inner_iter, outer_iter
#
#         if dx + dy > 0:
#             now_x, now_y = 0, 0
#         else:
#             now_x, now_y = -1, -1
#
#         start_x, start_y = now_x, now_y
#         for _ in range(outer_iter):
#             for __ in range(inner_iter):
#                 now_x, now_y = now_x + dx, now_y + dy
#                 if cheeses[now_x][now_y]:
#                     edges.add((now_x, now_y))
#                     break
#
#             start_x, start_y = start_x + dy, start_y + dx
#             now_x, now_y = start_x, start_y
#
#         if edges == set():
#             return 0
#
#     for x, y in edges:
#         cheeses[x][y] = 0
#
#     length = len(edges)
#     edges.clear()
#     return length
#
#
# rows, cols = map(int, input().split())
# cheeses = [list(map(int, input().split())) for _ in range(rows)]
# rows -= 1
# cols -= 1
# directions = ((1, 0), (0, 1), (-1, 0), (0, -1))
# edges = set()
# cnt = 0
# number_of_cheese = 0
# while True:
#     print(*cheeses, sep='\n')
#     print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
#     num = melt()
#     if not num:
#         print(cnt)
#         print(number_of_cheese)
#         break
#
#     cnt += 1
#     number_of_cheese = num


# ver 3
rows, cols = map(int, input().split())
cheeses = [list(map(int, input().split())) for _ in range(rows)]
cheeses[0][0] = 2
directions = ((1, 0), (0, 1), (-1, 0), (0, -1))
stack = [(0, 0)]
interfaces = set()
last = 0
while stack:
    last = len(stack)
    while stack:
        x, y = stack.pop()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if not 0 <= nx < rows or not 0 <= ny < cols:
                continue

            if cheeses[nx][ny] == 0:
                cheeses[nx][ny] = cheeses[x][y]
                stack.append((nx, ny))
            elif cheeses[nx][ny] == 1:
                cheeses[nx][ny] = cheeses[x][y] + 1
                interfaces.add((nx, ny))

    stack = list(interfaces)
    interfaces = set()

print(cheeses[x][y] - 2)
print(last)
