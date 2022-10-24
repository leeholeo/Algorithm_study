# import heapq
#
#
# # bfs using heap
# def lorry():
#     while heap:
#         time, r, c = heapq.heappop(heap)
#         roads[r][c] = time
#         nt = time + 1
#         for dr, dc in directions:
#             nr, nc = r + dr, c + dc
#             if not (0 <= nr < m and 0 <= nc < n):
#                 continue
#
#             nroad = roads[nr][nc]
#             if nroad == '.':
#                 continue
#             elif nroad == 'B':
#                 return nt - 10
#             elif nroad == '#':
#                 heapq.heappush(heap, (nt, nr, nc))
#             # junction
#             elif nroad < 10:
#                 remainder_time = (time - 10) % sum(junctions_time[nroad])
#                 first_time = junctions_time[nroad][first_verticals[nroad]]
#                 time_difference = remainder_time - first_time
#                 is_first = time_difference < 0
#                 if is_first == first_verticals[nroad]:
#                     is_vertical = True
#                 else:
#                     is_vertical = False
#
#                 # can go
#                 if (dr and is_vertical) or (dc and not is_vertical):
#                     heapq.heappush(heap, (nt, nr, nc))
#                 # cannot go
#                 else:
#                     if is_first:
#                         nt -= time_difference
#                     else:
#                         nt += sum(junctions_time[nroad]) - time_difference - first_time
#                     heapq.heappush(heap, (nt, nr, nc))
#     else:
#         return "impossible"
#
#
# m, n = map(int, input().split())
# directions = ((1, 0), (0, 1), (-1, 0), (0, -1))
# while m != 0 and n != 0:
#     # MAP input
#     roads = [' '.join(input()).split() for _ in range(m)]
#     junction_cnt = 0
#     for r in range(m):
#         for c in range(n):
#             if roads[r][c] == '#' or roads[r][c] == '.':
#                 continue
#             elif roads[r][c] == 'A':
#                 A_idx = (r, c)
#             elif roads[r][c] == 'B':
#                 B_idx = (r, c)
#             else:
#                 roads[r][c] = int(roads[r][c])
#                 junction_cnt += 1
#
#     # junctions information input
#     junctions_time = []
#     first_verticals = []
#     for _ in range(junction_cnt):
#         idx, drc, hor, ver = input().split()
#         if drc == '|':
#             first_verticals.append(1)
#         else:
#             first_verticals.append(0)
#
#         junctions_time.append((int(hor), int(ver)))
#
#     heap = []
#     heapq.heappush(heap, (10, A_idx[0], A_idx[1]))  # start at 10
#     print(lorry())
#     input()
#     m, n = map(int, input().split())


import heapq


# bfs using heap
def lorry():
    while heap:
        time, r, c = heapq.heappop(heap)
        roads[r][c] = time
        nt = time + 1
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if not (0 <= nr < m and 0 <= nc < n):
                continue

            nroad = roads[nr][nc]
            if nroad == '.':
                continue
            elif nroad == 'B':
                return nt - 10
            elif nroad == '#':
                heapq.heappush(heap, (nt, nr, nc))
            # junction
            elif nroad < 10:
                remainder_time = (time - 10) % sum(junctions_time[nroad])
                first_time = junctions_time[nroad][first_verticals[nroad]]
                time_difference = remainder_time - first_time
                is_first = time_difference < 0
                if is_first == first_verticals[nroad]:
                    is_vertical = True
                else:
                    is_vertical = False

                # can go
                if (dr and is_vertical) or (dc and not is_vertical):
                    heapq.heappush(heap, (nt, nr, nc))
                # cannot go
                else:
                    if is_first:
                        jt = nt - time_difference
                    else:
                        jt = nt + sum(junctions_time[nroad]) - time_difference - first_time
                    heapq.heappush(heap, (jt, nr, nc))
    else:
        return "impossible"


m, n = map(int, input().split())
directions = ((1, 0), (0, 1), (-1, 0), (0, -1))
while m != 0 and n != 0:
    # MAP input
    roads = [' '.join(input()).split() for _ in range(m)]
    junction_cnt = 0
    for r in range(m):
        for c in range(n):
            if roads[r][c] == '#' or roads[r][c] == '.':
                continue
            elif roads[r][c] == 'A':
                A_idx = (r, c)
            elif roads[r][c] == 'B':
                B_idx = (r, c)
            else:
                roads[r][c] = int(roads[r][c])
                junction_cnt += 1

    # junctions information input
    junctions_time = []
    first_verticals = []
    for _ in range(junction_cnt):
        idx, drc, hor, ver = input().split()
        if drc == '|':
            first_verticals.append(1)
        else:
            first_verticals.append(0)

        junctions_time.append((int(hor), int(ver)))

    heap = []
    heapq.heappush(heap, (10, A_idx[0], A_idx[1]))  # start at 10
    print(lorry())
    input()
    m, n = map(int, input().split())
