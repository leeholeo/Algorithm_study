def palindrome(end, start, now):
    if start == 0:
        start_num = 1
    else:
        start_num = 0

    if end - start < 2:
        if end - start == 1:
            for num in range(start_num, 10):
                palins.append(now + (10 ** end + 10 ** start) * num)
        elif end - start == 0:
            for num in range(start_num, 10):
                palins.append(now + 10 ** start * num)

        return

    for num in range(start_num, 10):
        palindrome(end - 1, start + 1, now + (10 ** end + 10 ** start) * num)


def palindromes():
    for length in range(a_len - 1, b_len):
        palindrome(length, 0, 0)


a_str, b_str = input().split()
a = int(a_str)
b = int(b_str)
a = max(a, 2)
a = min(a, b)
prime_limit = int(b ** 0.5 + 1)
Eratosthenes = [1] * prime_limit
primes = []
for n in range(2, prime_limit):
    if Eratosthenes[n]:
        primes.append(n)
        for m in range(1, (prime_limit - 1) // n + 1):
            Eratosthenes[n * m] = 0

a_len = len(a_str)
b_len = len(b_str)
palins = []
palindromes()

for i in range(len(palins)):
    if palins[i] >= a:
        palins = palins[i:]
        break

for i in range(len(palins) - 1, -1, -1):
    if palins[i] <= b:
        palins = palins[:i + 1]
        break

for i in range(len(palins)):
    if palins[i] >= prime_limit - 1:
        palins = palins[i:]
        break

    if palins[i] in primes:
        print(palins[i])

for pal in palins:
    for prime in primes:
        if not pal % prime:
            break
    else:
        print(pal)

print(-1)


# a_sh, a_re = divmod(a_len, 2)
# b_sh, b_re = divmod(a_len, 2)
# a_h_a_l_f = []
# b_h_a_l_f = []
# for i in range(a_sh, a_len):
#     if a_str[a_len - a_sh] > a_str[i]:
#         break
#     elif a_str[a_len - a_sh] == a_str[i]:
#         continue
#     else:
#         a_h_a_l_f = list(map(int, list(str(int(a_str[:a_sh + a_re]) + 1).split())))
#         break
#
# if not a_h_a_l_f:
#     a_h_a_l_f = [int(a_str[i]) for i in range(a_sh + a_re)]
#
#
# b_h_a_l_f = [int(b_str[i]) for i in range(b_sh + b_re)]