N = int(input())
pillars = [tuple(map(int, input().split())) for _ in range(N)]
pillars.sort()


def cover(rng):
    accum_pillars = [pillars[N-1-rng[-1]]]
    for i in rng:
        if accum_pillars[-1][1] < pillars[i][1]:
            accum_pillars.append(pillars[i])

    return accum_pillars


right_pillars = cover(range(N))
left_pillars = cover(range(N-1, -1, -1))
x, y = left_pillars[-1]
right_pillars.append((x+1, y))


def calculate_area(lst):
    area = 0
    for i in range(len(lst)-1):
        area += lst[i][1] * (lst[i+1][0] - lst[i][0])

    return area


print(calculate_area(right_pillars) - calculate_area(left_pillars))
