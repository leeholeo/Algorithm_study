primes = [7, 11, 13, 17, 19, 23, 29]
# 소수 확인
def prime_check(n):
    index = 0
    check_to = int(n ** (1 / 2))
    while primes[index] < check_to:
        if not n % primes[index]:
            break
    else:
        return True

    return False


# n 이하 소수 찾는 함수
def primes_to_n(n):
    multiple_3_cnt = 1
    for num in range(31, n, 2):
        multiple_3_cnt = (multiple_3_cnt + 1) % 3
        if multiple_3_cnt == 0:
            continue

        num_per_10 = num % 10
        if num_per_10 == 5 or num_per_10 == 0:
            continue

        if prime_check(num):
            primes.append(num)


# palindrome 확인
def pal_check(n):
    n = str(n)
    for i in range(len(n) // 2 + 1):
        if n[i] != n[-(i+1)]:
            return False

    return True


# n 이후 소수 찾는 함수
def pal_prime_after_n(n):
    multiple_3_cnt = n % 3
    num = n
    while True:
        num += 2
        multiple_3_cnt = (multiple_3_cnt + 1) % 3
        if multiple_3_cnt == 0:
            continue

        num_per_10 = num % 10
        if num_per_10 == 5 or num_per_10 == 0:
            continue

        if prime_check(num):
            if pal_check(num):
                return num
            else:
                primes.append(num)



N = int(input())
if N < 30:
    for i in range(len(primes)):
        if N < primes[i]:
            primes = primes[:i]
            break
else:
    primes_to_n(N)

ans = 0
print(pal_prime_after_n(N))
