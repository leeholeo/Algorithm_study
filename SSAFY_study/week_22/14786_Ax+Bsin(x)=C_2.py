'''
binary search
'''
import math


def formula(x):
    return A*x + B*math.sin(x)


def is_equal(a, b):
    return 0 <= abs(b-a) < 0.000000001


A, B, C = map(int, input().split())
left_end = C/A - math.pi/2
right_end = C/A + math.pi/2
div_num = 10
minus_x = None
minus_diff = None
plus_x = None
plus_diff = None
while not (minus_x and plus_x):
    div_len = (right_end-left_end)/div_num
    for mul in range(div_num+1):
        if minus_x and plus_x:
            break
        x = left_end + mul*div_len
        diff = formula(x) - C
        if diff < 0:
            if minus_x is None:
                minus_x = x
                minus_diff = diff
            else:
                if minus_diff < diff:
                    minus_x = x
                    minus_diff = diff
        else:
            if plus_x is None:
                plus_x = x
                plus_diff = diff
            else:
                if plus_diff > diff:
                    plus_x = x
                    plus_diff = diff
    div_num *= 10
half_x = (minus_x+plus_x)/2
diff = formula(half_x) - C
while is_equal(diff, 0) is False:
    if diff < 0:
        minus_x = half_x
        minus_diff = diff
    else:
        plus_x = half_x
        plus_diff = diff
    half_x = (minus_x + plus_x) / 2
    diff = formula(half_x) - C
print(half_x)
