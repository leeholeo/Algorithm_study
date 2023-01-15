'''
'''
def log(under: int, number: int):
    if number % under:
        return 0
    return log(under, number//under) + 1


def ingredient(number: int):
    return log(2, number), -log(3, number), number


N = int(input())
B = list(map(ingredient, map(int, input().split())))
B.sort()
print(*map(lambda x: x[2], B))
