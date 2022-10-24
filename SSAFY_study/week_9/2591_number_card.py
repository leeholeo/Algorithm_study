'''
스터디 기출, dp
a b
  a b
    a b
      a b
        ...
'''
number = input()
a = 1
b = 1
for i in range(1, len(number)):
    c = 0   # 임시 변수(b)
    if int(number[i]) > 0:
        c += b
    if 10 <= int(number[i-1:i+1]) <= 34:
        c += a
    a, b = b, c
print(b)
