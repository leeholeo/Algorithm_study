'''
Sieve of Eratosthenes
Goldbach's conjecture
odd = 2 + 3 + even(sum of 2 primes)
even = even(sum of 2 primes) + even(sum of 2 primes)
'''
import bisect


N = int(input())
if N < 8:
    print(-1)
    quit()
    
    
# Sieve of Eratosthenes
def eratos(maximum):
    primes = []
    sieve = [True] * (maximum+1)
    for i in range(2, maximum):
        if sieve[i] is False:
            continue
        primes.append(i)
        for j in range(2, maximum//i + 1):
            sieve[i*j] = False
    return primes


primes = eratos(N)

# even to two primes
def seperate(even):
    max_prime_index = bisect.bisect_left(primes, N) - 1
    min_prime_index = 0
    now = primes[min_prime_index] + primes[max_prime_index]
    while now != even:
        if now > even:
            max_prime_index -= 1
        else:
            min_prime_index += 1
        now = primes[min_prime_index] + primes[max_prime_index]
    return [primes[min_prime_index], primes[max_prime_index]]


# Goldbach's conjecture
answer = []
first = None
if N % 2:
    answer = [2, 3]
    N -= 5
    answer += seperate(N)
else:
    N = N//2
    if N % 2:
        answer = seperate(N-1) + seperate(N+1)
    else:
        answer = seperate(N) * 2

print(*answer)
