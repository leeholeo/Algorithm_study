'''
조건을 만족하는 조합은 최소 공배수 / 최대 공약수 를 소인수분해한 후 인수의 종류를 적절히 분배하여 나온다.
따라서 최대 조합 개수를 따지기 위해서는 가장 다양한 인수를 가지고 있는 입력을 찾으면 된다.
최대 입력은 100,000,000이므로 가장 작은 소수들부터 따질 때
가장 작은 소수 9개 [2, 3, 5, 7, 11, 13, 17, 19, 23] 의 곱은 223,092,870이다.
따라서 최대 조합 개수는 2^7 = 128이다.
'''
A, B = map(int, input().split())
# if B % A:
#     print('Impossible')
multiple_of_factors = B // A
prime_factors = []
for f in range(2, int(B // A ** 0.5) + 1):
    if multiple_of_factors == 1:
        break

    cnt = 0
    while True:
        share, remainder = divmod(multiple_of_factors, f)
        if remainder:
            break

        multiple_of_factors = share
        cnt += 1

    if cnt:
        prime_factors.append(f ** cnt)

length = len(prime_factors) - 1
min_sum = B
small = 1
big = 1
if length != -1:
    for comb in range(2 ** length):
        a = prime_factors[-1]
        b = 1
        for i in range(length):
            if comb & 1 << i:
                a *= prime_factors[i]
            else:
                b *= prime_factors[i]

        if a + b < min_sum:
            min_sum = a + b
            small = min(a, b)
            big = max(a, b)

small *= A
big *= A
print(small, big)
