# def people_number():
#     for number in range(1, 10000):
#         max_diff = number
#         for aver in average:
#             if 0 < aver * number % 1000 <= 1000 - max_diff:
#                 break
#         else:
#             return number
#
#
# N = int(input())
# average = [int(input().replace('.', '')) for _ in range(N)]
# print(people_number())

'''
decimal.Decimal(3.14)는 3.140000000000000124344978758017532527446746826171875의 값을 가진다(python 공식문서)
따라서 max_diff를 구할 때 Decimal(0.001)이 아닌 Decimal('0.001')을 사용해야 한다.
ref. https://github.com/python/cpython/blob/main/Lib/_pydecimal.py#:~:text=def%20from_float(cls%2C%20f)%3A
'''

# 틀렸습니다.
# from decimal import Decimal
#
#
# def people_number():
#     for number in range(1, 10000):
#         max_diff = Decimal(0.001) * number
#         for aver in average:
#             if 0 < aver * number % 1 <= 1 - max_diff:
#                 break
#         else:
#             return number
#
#
# N = int(input())
# average = [Decimal(input()) for _ in range(N)]
# print(people_number())

# ---------------------------------------------
from decimal import Decimal


def people_number():
    for number in range(1, 10000):
        max_diff = Decimal('0.001') * number
        for aver in average:
            if 0 < aver * number % 1 <= 1 - max_diff:
                break
        else:
            return number


N = int(input())
average = [Decimal(input()) for _ in range(N)]
print(people_number())
