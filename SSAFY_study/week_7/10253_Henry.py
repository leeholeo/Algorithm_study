# 최대공약수
def GCF(a, b):
    while True:
        if b > a:
            a, b = b, a
        s, r = divmod(a, b)
        if r == 0:
            return b
        a = r


# 최소공배수
def LCM(a, b):
    return a * b // GCF(a, b)


testcase = int(input())
for tc in range(testcase):
    a, b = map(int, input().split())
    # 가장 작은 헨리수 찾아서 빼주기
    while True:
        share, remainder = divmod(b, a)
        if remainder:
            lcm = LCM(b, share+1)
            denominator_to_lcm = lcm // (share+1)
            a = a * (lcm // b) - denominator_to_lcm
            b = lcm
        else:
            break

    print(share)
