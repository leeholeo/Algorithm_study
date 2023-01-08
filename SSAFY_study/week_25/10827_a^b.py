'''
파이썬은 신이야
'''
import decimal
decimal.getcontext().prec = 10000
a, b = map(decimal.Decimal, input().split())
print(f"{a ** b:.100000f}".rstrip('0').rstrip('.'))